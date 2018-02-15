import copy

import click
import jinja2
import json
import os
from swagger_parser import SwaggerParser

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

BACKEND_CHOICES = ["django", "aiohttp"]


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
    template_directory = "./swagger_django_generator/templates/{}/".format(backend)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_directory),
        #loader=jinja2.PackageLoader("swagger_django_generator",
        #                            "templates/{}/".format(template_module)),
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

    def __init__(self, backend, module_name=DEFAULT_MODULE):
        self.backend = backend
        self.parser = None
        self.module_name = module_name
        self._classes = None

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

        self._make_class_definitions()

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

    def _make_class_definitions(self):
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
              help="Use an alternative filename for the utilities.")
def main(specification_path, spec_format, backend, verbose, output_dir, module_name,
         urls_file, views_file, schemas_file, utils_file, stubs_file):

    generator = Generator(backend, module_name=module_name)
    try:
        click.secho("Loading specification file...", fg="green")
        generator.load_specification(specification_path, spec_format)

        click.secho("Generating URLs file...", fg="green")
        with open(os.path.join(output_dir, urls_file), "w") as f:
            data = generator.generate_urls()
            f.write(data)
            if verbose:
                print(data)

        click.secho("Generating views file...", fg="green")
        with open(os.path.join(output_dir, views_file), "w") as f:
            data = generator.generate_views()
            f.write(data)
            if verbose:
                print(data)

        click.secho("Generating schemas file...", fg="green")
        with open(os.path.join(output_dir, schemas_file), "w") as f:
            data = generator.generate_schemas()
            f.write(data)
            if verbose:
                print(data)

        click.secho("Generating utils file...", fg="green")
        with open(os.path.join(output_dir, utils_file), "w") as f:
            data = generator.generate_utils()
            f.write(data)
            if verbose:
                print(data)

        click.secho("Generating stubs file...", fg="green")
        with open(os.path.join(output_dir, stubs_file), "w") as f:
            data = generator.generate_stubs()
            f.write(data)
            if verbose:
                print(data)

        click.secho("Done.", fg="green")
    except Exception as e:
        click.secho(e.message, fg="red")


if __name__ == "__main__":
    main()
