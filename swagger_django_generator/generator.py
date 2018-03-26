import copy
from collections import OrderedDict

import click
import inflect
import jinja2
import json
import os
import sys
from swagger_parser import SwaggerParser

words = inflect.engine()

DEFAULT_OUTPUT_DIR = "./generated"
DEFAULT_MODULE = "generated"

# Defaults used when the path is "/".
ROOT_CLASS_NAME = u"Root"
ROOT_OPERATION = u"root"

# Known extensions in lowercase
YAML_EXTENSIONS = ["yaml", "yml"]
JSON_EXTENSIONS = ["json"]

# Choices provided when specifying the specification format
SPEC_JSON = "json"
SPEC_YAML = "yaml"
SPEC_CHOICES = [SPEC_JSON, SPEC_YAML]

BACKEND_CHOICES = ["django"]
major, minor = sys.version_info[0:2]
if major > 3 or major == 3 and minor >= 5:
    BACKEND_CHOICES.append("aiohttp")
    BACKEND_CHOICES.append("aor")

# Component Mapping for swagger types to AOR components
COMPONENT_MAPPING = {
    "integer": "Number",
    "string": "Text",
    "boolean": "Boolean",
    "date-time": "Date",
    "enum": "Select"
}

COMPONENT_SUFFIX = {
    "list": "Field",
    "show": "Field",
    "create": "Input",
    "edit": "Input"
}

SUPPORTED_COMPONENTS = ["list", "show", "create", "edit"]

# from swagger_tester import swagger_test

# parser.base_path contains the base URL, e.g. "/portal/v1"
# parser.paths is a dictionary of the form:
# {
#   path: {
#       http_verb: {
#           "consumes": ["application/json"],
#           "produces": ["application/json"],
#           "responses": {
#               status_code: {
#                   "description": "",
#                   "schema": JSONSchema
#               },
#               ...
#           },
#           "parameters": {
#               name: {
#                   "description": "The description",
#                   "in": "path",
#                   "name": name,
#                   "required": True,
#                   "type": "string"
#               },
#               "body": {
#                   "description": "The message payload",
#                   "in": "body",
#                   "name": "body",
#                   "required": True,
#                   "schema": {
#                       "$ref": "#/definitions/message",
#                       "x-scope": [""]
#                   }
#               },
#               ...
#           },
#       },
#       ...
#
# parser.operation is a dictionary of the form:
# {operation: (path, http_verb, tag)}
#
# * Paths map to class based views.
# * (path, http_verb) combinations map to operations.


def render_to_string(backend, filename, context):
    # type: (str, str, Dict) -> str
    """
    Render a template using the specified context
    :param backend: The backend for which the template is rendered
    :param filename: The template name
    :param context: The data to use when rendering the template
    :return: The rendered template as a string
    """
    template_directory = "./swagger_django_generator/templates/{}".format(backend)
    loaders = [jinja2.FileSystemLoader(template_directory)]
    try:
        import swagger_django_generator
        loaders.append(jinja2.PackageLoader("swagger_django_generator", "templates/{}".format(backend)))
    except ImportError:
        pass

    return jinja2.Environment(
        loader=jinja2.ChoiceLoader(loaders),
        trim_blocks=True,
        lstrip_blocks=True
    ).get_template(filename).render(context)


def path_to_class_name(path):
    # type: (unicode) -> unicode
    """
    We map paths (typically only the relative part) to a canonical
    class name. In the event that the path is "/", ROOT_CLASS_NAME will be
    returned.
    :param path: A path of the form "/some/path/{foo_id}/bar/{barId}/"
    :return: A class name of the form "SomePathFooIdBarBarId"
    """
    character_map = {
        ord("{"): None,
        ord("}"): None,
        ord("_"): u"/"
    }
    sanitised = path.translate(character_map)
    class_name = u"".join(
        # Uppercase the first letter of each non-empty word, while
        # preserving the case of the letters thereafter.
        p[0].upper() + p[1:] for p in sanitised.split("/") if p
    )
    return class_name or ROOT_CLASS_NAME


def path_to_operation(path, verb):
    # type: (unicode, unicode) -> unicode
    """
    We map paths (typically only the relative part) to a canonical
    operation name. The operation name is used as the name of the function
    that must provide the server-side logic.
    Typically the operation name is provided in the Swagger space via the
    `operationId` field. This function is used as a fallback mechanism when
    it is not defined explicitly.
    :param path: A path of the form "/some/path/{id}/foo/{bar}/"
    :param verb: The HTTP verb, e.g. "get"
    :return: An operation name of the form "get_some_path_id_foo_bar"
    """
    character_map = {
        ord("{"): None,
        ord("}"): None,
        ord("_"): u"/"
    }
    if path == u"/":
        operation = ROOT_OPERATION
    else:
        sanitised = path.translate(character_map)
        operation = u"_".join(p for p in sanitised.split("/"))

    return "{}_{}".format(verb, operation)


def fixup_parameters(url, backend):
    """
    Parameters in the Swagger spec paths are wrapped in curly braces.
    We change these to a named regex match for use be Django.
    E.g. "/foo/{bar_id}/" => "/foo/(?P<bar_id>.+)/"
    :param url: The URL from the Swagger spec
    :param backend: The backend for which to generate the parameters
    :return: The URL with parameters changed into regexes.
    """
    result = url
    if backend == "django":
        result = url.replace("{", "(?P<").replace("}", ">.+)")

    return result


class Generator(object):
    PATH_VERB_OPERATION_MAP = {}

    def __init__(self, backend, output_dir, urls_file, views_file, schemas_file,
                 utils_file, stubs_file, module_name=DEFAULT_MODULE, verbose=False):
        self.backend = backend
        self.parser = None
        self.module_name = module_name
        self._resources = None
        self._classes = None
        self.verbose = verbose
        self.output_dir = output_dir
        self.urls_file = urls_file
        self.views_file = views_file
        self.schemas_file = schemas_file
        self.utils_file = utils_file
        self.stubs_file = stubs_file

    def load_specification(self, specification_path, spec_format=None):
        # If the swagger spec format is not specified explicitly, we try to
        # derive it from the specification path
        if not spec_format:
            filename = os.path.basename(specification_path)
            extension = filename.rsplit(".", 1)[-1]
            if extension in YAML_EXTENSIONS:
                spec_format = SPEC_YAML
            elif extension in JSON_EXTENSIONS:
                spec_format = SPEC_JSON
            else:
                raise RuntimeError("Could not infer specification format. Use "
                                   "--spec-format to specify it explicitly.")

        click.secho("Using spec format '{}'".format(spec_format), fg="green")
        if spec_format == SPEC_YAML:
            with open(specification_path, "r") as f:
                self.parser = SwaggerParser(swagger_yaml=f)
        else:
            self.parser = SwaggerParser(swagger_path=specification_path)

        # Build (path, http_verb) => operation mapping
        self.PATH_VERB_OPERATION_MAP = {
            (path, http_verb): operation
            for operation, (path, http_verb, tag) in
            self.parser.operation.items()
        }

    def generate_specification(self):
        if self.backend == "aor":
            self._make_aor_resource_definitions()
        else:
            self._make_django_class_definitions()

    def resolve_schema_references(self, definition):
        # type: (Generator, Dict) -> None
        """
        JSONSchema definitions may contain references.
        This function replaces all references with their full definitions.
        In-place mods are made.

        :param definition: A JSONSchema definition
        :return: The expended definition.
        """
        if "$ref" in definition:
            schema_reference = definition.pop("$ref")
            section, name = schema_reference.split("/")[-2:]
            referenced_definition = self.parser.specification[section][name]
            definition.update(referenced_definition)

        for value in definition.values():
            if isinstance(value, dict):
                self.resolve_schema_references(value)

    def _get_definition_from_ref(self, definition):
        if "$ref" in definition:
            definition_name = \
                self.parser.get_definition_name_from_ref(definition["$ref"])
            ref_def = self.parser.specification["definitions"][definition_name]
            title = definition_name.replace("_", " ").title().replace(" ", "")
            return ref_def, title
        else:
            return definition, None

    def _get_resource_from_definition(self, resource_name, head_component,
                                      definition):
        resource = []
        suffix = COMPONENT_SUFFIX[head_component]
        properties = OrderedDict(definition.get("properties", {}))
        for name, details in properties.items():
            attribute = {
                "source": name,
                "type": details.get("type", None),
                "required": name in definition.get("required", []),
                "read_only": details.get("readOnly", False)
            }
            # Based on the type/format combination get the correct
            # AOR component to use.
            if details.get("format", None) in COMPONENT_MAPPING:
                attribute["component"] = \
                    COMPONENT_MAPPING[details["format"]] + suffix
            elif attribute["type"] in COMPONENT_MAPPING:
                attribute["component"] = \
                    COMPONENT_MAPPING[attribute["type"]] + suffix
            # Handle an enum possibility
            if details.get("enum", None) is not None:
                attribute["component"] = COMPONENT_MAPPING["enum"] + suffix
                attribute["choices"] = details["enum"]

            if attribute.get("component", None) is not None:
                # Add component to resource imports if not there.
                if attribute["component"] not in \
                        self._resources[resource_name]["imports"]:
                    self._resources[resource_name]["imports"].append(
                        attribute["component"]
                    )
                resource.append(attribute)
        # Only add if there is something in resource
        if resource:
            self._resources[resource_name][head_component] = resource

    def _fix_composite_ids(self, composite_parameters):
        # Go through each resources components and check if they are
        # Composite parameters.
        for resource in self._resources.values():
            composites = composite_parameters.get(resource["path"], None)
            if composites is None:
                continue
            resource["composite_parameters"] = composites
            for action, attributes in resource.items():
                if action in SUPPORTED_COMPONENTS:
                    suffix = COMPONENT_SUFFIX[action]
                    for attribute in attributes:
                        if attribute["source"] in composites:
                            old_component = attribute["component"]
                            attribute["component"] = "Reference" + suffix
                            relation = attribute["source"].replace("_id", "")
                            attribute["label"] = relation.title()
                            attribute["reference"] = words.plural(relation)
                            if suffix != "Input":
                                attribute["related_component"] = old_component
                            else:
                                attribute["related_component"] = "SelectInput"

    def _make_aor_resource_definitions(self):
        self._resources = {}
        # Get all composite ID parameters for each resource.
        composite_parameters = {}
        for path, verbs in self.parser.specification["paths"].items():
            # Get base path and load all composite parameters for the same
            # base_path.
            base_path = path[1:].split("/")[0]
            if base_path not in composite_parameters:
                composite_parameters[base_path] = {}
            for parameter in verbs.get("parameters", []):
                if "$ref" in parameter:
                    ref = parameter["$ref"].split("/")[2]
                    param = self.parser.specification["parameters"][ref]
                else:
                    param = parameter
                if "id" in param.get("name", []) and param.get("name", None) != "id":
                    composite_parameters[base_path][param["name"]] = param["type"]

            # If there is only one ID parameter, it is not a group of composites.
            # Therefore clear it.
            if len(composite_parameters[base_path]) < 2:
                composite_parameters.pop(base_path)

            for verb, io in verbs.items():

                # Check if this is not a method.
                if verb == "parameters":
                    continue
                elif not io.get("operationId", None):
                    continue

                # Get resource name and path and add it to the list
                # for the first occurring instance of the resource
                operation_id = io["operationId"]
                name = operation_id.split("_")[0]
                if name not in self._resources:
                    self._resources[name] = {
                        "path": base_path,
                        "imports": [],
                        "has_methods": False
                    }

                definition = None
                head_component = None

                # Get the correct definition/head_component/component suffix per
                # verb based on the operation.
                _create = "create" in operation_id
                _update = "update" in operation_id
                if "read" in operation_id:
                    definition, title = self._get_definition_from_ref(
                        definition=io["responses"]["200"]["schema"]
                    )
                    self._resources[name]["title"] = title or name
                    head_component = "show"
                elif "list" in operation_id:
                    definition, title = self._get_definition_from_ref(
                        definition=io["responses"]["200"]["schema"]["items"]
                    )
                    head_component = "list"
                elif _create or _update:
                    for parameter in io.get("parameters", []):
                        param = parameter["$ref"] \
                            if "$ref" in parameter else parameter
                        # Grab the body parameter as the create definition
                        if param["in"] == "body":
                            definition, title = self._get_definition_from_ref(
                                definition=param["schema"]
                            )
                    head_component = "create" if _create else "edit"
                if head_component and definition:
                    # Toggle to be included in AOR if it has a single method.
                    self._resources[name]["has_methods"] = True
                    self._get_resource_from_definition(
                        resource_name=name,
                        head_component=head_component,
                        definition=definition
                    )

        self._fix_composite_ids(composite_parameters=composite_parameters)
        self.aor_generation()

    def _make_django_class_definitions(self):
        self._classes = {}
        for path, verbs in self.parser.paths.items():
            relative_url = path.replace(self.parser.base_path, "")
            class_name = path_to_class_name(relative_url)
            self._classes[class_name] = {}
            for verb, io in verbs.items():  # io => input/output options
                # Look up the name of the operation and construct one if not found
                operation = self.PATH_VERB_OPERATION_MAP.get(
                    (path, verb), path_to_operation(path, verb)
                )
                payload = {
                    "operation": operation,
                    "required_args": [],
                    "optional_args": [],
                    "form_data": [],
                    "response_schema": "schemas.__UNSPECIFIED__",
                    "secure": False,
                }

                # Add arguments
                for name, detail in io["parameters"].items():
                    location = detail["in"]
                    if location == "path":
                        section = "required_args" if detail["required"] else \
                            "optional_args"
                        payload[section].append(detail)
                    elif location == "query":
                        section = "required_args" if detail["required"] else \
                            "optional_args"
                        payload[section].append(detail)
                    elif location == "body":
                        # There cannot be more than one body parameter
                        payload["body"] = copy.deepcopy(detail)
                        schema = payload["body"]["schema"]
                        schema_reference = schema.get("$ref", None)
                        if schema_reference:
                            # TODO: Fix this crude lookup code
                            # It expects a reference to have the form
                            # "#/definitions/name"
                            lookup = schema_reference.split("/")[-1]
                            payload["body"]["schema"] = "schemas.{}".format(
                                lookup)
                        else:
                            # Inline schema definitions do not reference the
                            # schema module. For now the definitions are
                            # (inefficiently) inlined in the generated
                            # view. TODO: Optimise by loading these schemas
                            # on initialisation and referencing it thereafter.
                            # Also, we it would be nice to be able to reference
                            # the definitions in schemas.py...will significantly
                            # reduce size of the generated code in views.py.
                            self.resolve_schema_references(schema)
                            payload["body"]["schema"] = \
                                'json.loads("""{}""")'.format(
                                    json.dumps(schema, indent=4, sort_keys=True)
                                )
                    elif location == "formData":
                        payload["form_data"].append(detail)
                    else:
                        msg = "Code generation for parameter type '{}' not " \
                              "implemented yet. Operation '{}' parameter '{" \
                              "}'".format(location, operation, name)
                        click.secho(msg, fg="red")

                # Added response
                for name, detail in io["responses"].items():
                    if name == "default":
                        continue
                    elif 200 <= int(name) < 300 and "schema" in detail:
                        # There should only be one response code defined in
                        # the 200 to 299 range.
                        schema = copy.deepcopy(detail["schema"])
                        schema_reference = schema.get("$ref", None)
                        if schema_reference:
                            # TODO: Fix this crude lookup code
                            # It expects a reference to have the form
                            # "#/definitions/name"
                            lookup = schema_reference.split("/")[-1]
                            payload["response_schema"] = "schemas.{}".format(lookup)
                        else:
                            # Inline schema definitions do not reference the
                            # schema module. For now the definitions are
                            # (inefficiently) inlined in the generated
                            # view. TODO: Optimise by loading these schemas
                            # on initialisation and referencing it thereafter.
                            # Also, we it would be nice to be able to reference
                            # the definitions in schemas.py...will significantly
                            # reduce size of the generated code in views.py.
                            self.resolve_schema_references(schema)
                            payload["response_schema"] = \
                                'json.loads("""{}""")'.format(
                                    json.dumps(schema, indent=4, sort_keys=True)
                                )

                # TODO: At this stage we do not look at the type of security, we
                # simply flag that it should be secured.
                # Also, the parser does not contain the security info,
                # so we have to refer back to the original spec.
                if "security" in self.parser.specification:
                    # Global security indicator
                    payload["secure"] = True
                else:
                    # Path and verb specific indicator
                    specref = self.parser.specification["paths"].get(
                        relative_url, {}
                    ).get(verb, {})
                    payload["secure"] = "security" in specref

                self._classes[class_name][verb] = payload
        self.django_aiohttp_generation()

    def generate_urls(self):
        # type: (Generator) -> str
        """
        Generate a `urls.py` file from the given specification.
        :return: str
        """
        relative_urls = [path.replace(self.parser.base_path + "/", "")
                         for path in self.parser.paths]
        entries = {
            fixup_parameters(relative_url, self.backend): path_to_class_name(relative_url)
            for relative_url in relative_urls
        }
        return render_to_string(
            self.backend, "urls.py", {
                "entries": entries,
                "module": self.module_name
            })

    def generate_schemas(self):
        # type: (Generator) -> str
        """
        Generate a `schemas.py` file from the given specification.
        :return: str
        """
        schemas = {}
        for name, definition in self.parser.specification.get("definitions",
                                                              {}).items():
            schema = copy.deepcopy(definition)
            self.resolve_schema_references(schema)
            schemas[name] = json.dumps(schema, indent=4, sort_keys=True)

        return render_to_string(
            self.backend, "schemas.py", {
                "schemas": schemas,
                "module": self.module_name
            })

    def generate_views(self):
        # type: (Generator) -> str
        """
        Generate a `views.py` file from the given specification.
        :return: str
        """
        return render_to_string(
            self.backend, "views.py", {
                "classes": self._classes,
                "module": self.module_name,
                "specification": json.dumps(self.parser.specification, indent=4,
                                            sort_keys=True).replace("\\", "\\\\")
            })

    def generate_stubs(self):
        # type: (Generator) -> str
        """
        Generate a `stubs.py` file from the given specification.
        :return: str
        """
        return render_to_string(
            self.backend, "stubs.py", {
                "classes": self._classes,
                "module": self.module_name
            })

    def generate_utils(self):
        # type: (Generator) -> str
        """
        Generate a `utils.py` file from the given specification.
        :return: str
        """
        return render_to_string(self.backend, "utils.py", {})

    def generate_app_js(self):
        """
        Generate an `App.js` file from the given specification.
        :return: str
        """
        return render_to_string(self.backend, "App.js", {
            "title": self.module_name,
            "resources": self._resources,
            "supported_components": SUPPORTED_COMPONENTS
        })

    def generate_resource_js(self, name, resource):
        """
        Generate a single resource component file.
        :return: str
        """
        return render_to_string(self.backend, "Resource.js", {
            "name": name,
            "resource": resource,
            "supported_components": SUPPORTED_COMPONENTS
        })

    def generate_swagger_rest_server_js(self):
        """
        Generate a generic swagger rest server file.
        :return: str
        """
        # Check if there are composite ids in any resource.
        has_composites = False
        for resource in self._resources.values():
            if "composite_parameters" in resource:
                has_composites = True
                break
        return render_to_string(self.backend, "swaggerRestServer.js", {
            "resources": self._resources,
            "has_composites": has_composites
        })

    def aor_generation(self):
        click.secho("Generating App.js component file...", fg="green")
        with open(os.path.join(self.output_dir, "App.js"), "w") as f:
            data = self.generate_app_js()
            f.write(data)
            if self.verbose:
                print(data)
        click.secho("Generating resource component files...", fg="green")
        for name, resource in self._resources.items():
            title = resource.get("title", None)
            if title:
                click.secho("Generating {}.js file...".format(title), fg="green")
                with open(os.path.join(self.output_dir, "{}.js".format(title)), "w") as f:
                    data = self.generate_resource_js(title, resource)
                    f.write(data)
                    if self.verbose:
                        print(data)
        click.secho("Generating basic swagger rest server file...", fg="green")
        with open(os.path.join(self.output_dir, "swaggerRestServer.js"), "w") as f:
            data = self.generate_swagger_rest_server_js()
            f.write(data)
            if self.verbose:
                print(data)

    def django_aiohttp_generation(self):
        click.secho("Generating URLs file...", fg="green")
        with open(os.path.join(self.output_dir, self.urls_file), "w") as f:
            data = self.generate_urls()
            f.write(data)
            if self.verbose:
                print(data)

        click.secho("Generating views file...", fg="green")
        with open(os.path.join(self.output_dir, self.views_file), "w") as f:
            data = self.generate_views()
            f.write(data)
            if self.verbose:
                print(data)

        click.secho("Generating schemas file...", fg="green")
        with open(os.path.join(self.output_dir, self.schemas_file), "w") as f:
            data = self.generate_schemas()
            f.write(data)
            if self.verbose:
                print(data)

        click.secho("Generating utils file...", fg="green")
        with open(os.path.join(self.output_dir, self.utils_file), "w") as f:
            data = self.generate_utils()
            f.write(data)
            if self.verbose:
                print(data)

        click.secho("Generating stubs file...", fg="green")
        with open(os.path.join(self.output_dir, self.stubs_file), "w") as f:
            data = self.generate_stubs()
            f.write(data)
            if self.verbose:
                print(data)


@click.command()
@click.argument("specification_path", type=click.Path(dir_okay=False, exists=True))
@click.option("--spec-format", type=click.Choice(SPEC_CHOICES))
@click.option("--backend", type=click.Choice(BACKEND_CHOICES),
              default="django")
@click.option("--verbose/--no-verbose", default=False)
@click.option("--output-dir", type=click.Path(file_okay=False, exists=True,
                                              writable=True),
              default=DEFAULT_OUTPUT_DIR)
@click.option("--module-name", type=str, default=DEFAULT_MODULE,
              help="The name of the module where the generated code will be "
                   "used, e.g. myproject.some_application")
@click.option("--urls-file", type=str, default="urls.py",
              help="Use an alternative filename for the urls.")
@click.option("--views-file", type=str, default="views.py",
              help="Use an alternative filename for the views.")
@click.option("--schemas-file", type=str,  default="schemas.py",
              help="Use an alternative filename for the schemas.")
@click.option("--utils-file", type=str,  default="utils.py",
              help="Use an alternative filename for the utilities.")
@click.option("--stubs-file", type=str,  default="stubs.py",
              help="Use an alternative filename for the stubs.")
def main(specification_path, spec_format, backend, verbose, output_dir, module_name,
         urls_file, views_file, schemas_file, utils_file, stubs_file):

    generator = Generator(
        backend, output_dir, urls_file, views_file, schemas_file,
        utils_file, stubs_file, module_name=module_name, verbose=verbose
    )
    try:
        click.secho("Loading specification file...", fg="green")
        generator.load_specification(specification_path, spec_format)
        generator.generate_specification()
        click.secho("Done.", fg="green")
    except Exception as e:
        click.secho(str(e), fg="red")
        click.secho("""
        If you get schema validation errors from a yaml Swagger spec that passes validation on other
        validators, it may be because of single apostrophe's (') used in some descriptions. The
        parser used does not like it at all.
        """)


if __name__ == "__main__":
    main()
