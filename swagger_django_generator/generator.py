import click
import jinja2
import json
import os
from pprint import pprint
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


global PATH_VERB_OPERATION_MAP

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


def render_to_string(filename, context, path=None):
    # type: (str, Dict, str) -> str
    """
    Render a template using the specified context
    :param filename: The template name
    :param context: The data to use when rendering the template
    :param path: An optional path to load the template from
    :return: The rendered template as a string
    """
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './'),
        trim_blocks=True,
        lstrip_blocks=True
    ).get_template(filename).render(context)


def path_to_class_name(path):
    # type: (unicode) -> unicode
    """
    We map paths (typically only the relative part) to a canonical
    class name. In the event that the path is "/", ROOT_CLASS_NAME will be
    returned.
    :param path: A path of the form "/some/path/{id}/foo/{bar}/"
    :return: A class name of the form "SomePathIdFooBar"
    """
    character_map = {
        ord("{"): None,
        ord("}"): None,
        ord("_"): u"/"
    }
    sanitised = path.translate(character_map)
    class_name = u"".join(p.capitalize() for p in sanitised.split("/"))
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


def fixup_parameters(url):
    """
    Parameters in the Swagger spec paths are wrapped in curly braces.
    We change these to a named regex match for use be Django.
    E.g. "/foo/{bar_id}/" => "/foo/(?P<bar_id>.+)/"
    :param url: The URL from the Swagger spec
    :return: The URL with parameters changed into regexes.
    """
    return url.replace("{", "(?P<").replace("}", ">.+)")


def generate_urls(parser, module_name):
    # type: (SwaggerParser, str) -> str
    """
    Generate a `urls.py` file from the given specification.
    :param parser: The parsed specification
    :param module_name: The module name used in the generated code.
    :return: str
    """
    relative_urls = [path.replace(parser.base_path, "")
                     for path in parser.paths]
    entries = {
        fixup_parameters(relative_url): path_to_class_name(relative_url)
        for relative_url in relative_urls
    }
    return render_to_string("templates/urls.py", {
        "entries": entries,
        "module": module_name
    })


def generate_schemas(parser, module_name):
    # type: (SwaggerParser, str) -> str
    """
    Generate a `schemas.py` file from the given specification.
    :param parser: The parsed specification
    :param module_name: The module name used in the generated code.
    :return: str
    """
    schemas = {
        name: json.dumps(definition, indent=4, sort_keys=True)
        # name: pformat(definition, indent=1, width=76)
        for name, definition in parser.specification.get(
            "definitions", {}
        ).iteritems()
    }
    return render_to_string("templates/schemas.py", {
        "schemas": schemas,
        "module": module_name
    })


def generate_views(parser, module_name):
    # type: (SwaggerParser, str) -> str
    """
    Generate a `views.py` file from the given specification.
    :param parser: The parsed specification
    :param module_name: The module name used in the generated code.
    :return: str
    """
    global PATH_VERB_OPERATION_MAP
    classes = {}
    for path, verbs in parser.paths.iteritems():
        relative_url = path.replace(parser.base_path, "")
        class_name = path_to_class_name(relative_url)
        classes[class_name] = {}
        for verb, io in verbs.iteritems():  # io => input/output options
            # Look up the name of the operation and construct one if not found
            operation = PATH_VERB_OPERATION_MAP.get(
                (path, verb), path_to_operation(path, verb)
            )
            payload = {
                "operation": operation,
                "required_args": [],
                "optional_args": [],
            }
            for name, detail in io["parameters"].iteritems():
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
                    payload["body"] = detail
                    schema_reference = detail["schema"].get("$ref", None)
                    if schema_reference:
                        # TODO: Fix this crude lookup code
                        # It expects a reference to have the form
                        # "#/definitions/name"
                        lookup = schema_reference.split("/")[-1]
                        detail["schema"] = "schemas.{}".format(lookup)
                    else:
                        # Inline schema definition
                        detail["schema"] = json.dumps(detail["schema"])
                else:
                    msg = "Code generation for parameter type '{}' not " \
                          "implemented yet. Operation '{}' parameter '{" \
                          "}'".format(location, operation, name)
                    click.secho(msg, fg="red")

            classes[class_name][verb] = payload

    return render_to_string("templates/views.py", {
        "classes": classes,
        "module": module_name
    })


@click.command()
@click.argument("specification_path", type=click.Path(dir_okay=False,
                                                    exists=True))
@click.option("--spec-format", type=click.Choice(SPEC_CHOICES))
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
def main(specification_path, spec_format, verbose, output_dir, module_name,
         urls_file, views_file,
         schemas_file, utils_file):
    global PATH_VERB_OPERATION_MAP
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
            click.secho("Could not infer specification format. Use "
                        "--spec-format to specify it explicitly.")
            exit(0)

    if spec_format == SPEC_YAML:
        with open(specification_path, "r") as f:
            parser = SwaggerParser(swagger_yaml=f)
    else:
        parser = SwaggerParser(swagger_path=specification_path)

    # Build (path, http_verb) => operation mapping
    PATH_VERB_OPERATION_MAP = {
        (path, http_verb): operation
        for operation, (path, http_verb, tag) in parser.operation.iteritems()
    }

    click.secho("Generating URLs file...", fg="green")
    with open(os.path.join(output_dir, urls_file), "w") as f:
        data = generate_urls(parser, module_name)
        f.write(data)
        if verbose:
            print(data)

    click.secho("Generating views file...", fg="green")
    with open(os.path.join(output_dir, views_file), "w") as f:
        data = generate_views(parser, module_name)
        f.write(data)
        if verbose:
            print(data)

    click.secho("Generating schemas file...", fg="green")
    with open(os.path.join(output_dir, schemas_file), "w") as f:
        data = generate_schemas(parser, module_name)
        f.write(data)
        if verbose:
            print(data)

    click.secho("Generating utils file...", fg="green")
    with open(os.path.join(output_dir, utils_file), "w") as f:
        data = render_to_string("templates/utils.py", {})
        f.write(data)
        if verbose:
            print(data)

    click.secho("Done.", fg="green")


if __name__ == "__main__":
    main()
