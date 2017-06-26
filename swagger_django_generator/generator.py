import click
import jinja2
import json
import os
from pprint import pprint
from swagger_parser import SwaggerParser

DEFAULT_OUTPUT_DIR = "./generated"
DEFAULT_MODULE = "generated"
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
    class name.
    :param path: A path of the form "/some/path/{id}/foo/{bar}/"
    :return: A class name of the form "SomePathIdFooBar"
    """
    character_map = {
        ord("{"): None,
        ord("}"): None,
        ord("_"): u"/"
    }
    sanitised = path.translate(character_map)
    return u"".join(p.capitalize() for p in sanitised.split("/"))


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
        for name, definition in parser.specification["definitions"].iteritems()
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
    classes = {}
    for path, verbs in parser.paths.iteritems():
        relative_url = path.replace(parser.base_path, "")
        class_name = path_to_class_name(relative_url)
        classes[class_name] = {}
        for verb, io in verbs.iteritems():  # io => input/output options
            payload = {
                "operation": PATH_VERB_OPERATION_MAP[(path, verb)],
                "required_args": [],
                "optional_args": [],
            }
            for name, detail in io["parameters"].iteritems():
                if detail["in"] == "path":
                    section = "required_args" if detail["required"] else \
                        "optional_args"
                    payload[section].append(detail)
                elif detail["in"] == "body":
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

            classes[class_name][verb] = payload

    return render_to_string("templates/views.py", {
        "classes": classes,
        "module": module_name
    })


@click.command()
@click.argument("specification", type=click.File("r"))
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
def main(specification, verbose, output_dir, module_name, urls_file, views_file,
         schemas_file):
    global PATH_VERB_OPERATION_MAP
    parser = SwaggerParser(swagger_yaml=specification)

    # Build (path, http_verb) => operation mapping
    PATH_VERB_OPERATION_MAP = {
        (path, http_verb): operation
        for operation, (path, http_verb, tag) in parser.operation.iteritems()
    }

    with open(os.path.join(output_dir, urls_file), "w") as f:
        data = generate_urls(parser, module_name)
        f.write(data)
        if verbose:
            print(data)

    with open(os.path.join(output_dir, views_file), "w") as f:
        data = generate_views(parser, module_name)
        f.write(data)
        if verbose:
            print(data)

    with open(os.path.join(output_dir, schemas_file), "w") as f:
        data = generate_schemas(parser, module_name)
        f.write(data)
        if verbose:
            print(data)


if __name__ == "__main__":
    main()
