"""
Do not modify this file. It is generated from the Swagger specification.

"""
import importlib
import logging
import json
import jsonschema
import os
from jsonschema import ValidationError
from aiohttp.web import View, json_response, Response, HTTPNoContent
from aiohttp_cors import CorsViewMixin

import {{ module }}.schemas as schemas
import {{ module }}.utils as utils

# Set up logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

VALIDATE_RESPONSES = os.getenv("SWAGGER_API_VALIDATE_RESPONSES", False)
LOGGER.info("Swagger API response validation is {}".format(
    "on" if VALIDATE_RESPONSES else "off"
))

# Set up the stub class. If it is not explicitly configured in the settings.py
# file of the project, we default to a mocked class.
stub_class_path = os.getenv("STUBS_CLASS", "{{ module }}.stubs.MockedStubClass")
module_name, class_name = stub_class_path.rsplit(".", 1)
Module = importlib.import_module(module_name)
Stubs = getattr(Module, class_name)


def maybe_validate_result(result, schema):
    if VALIDATE_RESPONSES:
        try:
            utils.validate(result, schema)
        except ValidationError as e:
            LOGGER.error(e.message)


{% for class_name, verbs in classes|dictsort(true) %}
{# @method_decorator(csrf_exempt, name="dispatch") #}
{% for verb, info in verbs|dictsort(true) %}
{% if info.secure %}
{# @method_decorator(utils.login_required_no_redirect, name="{{ verb }}") #}
{% endif %}
{% endfor %}
class {{ class_name }}(View, CorsViewMixin):

    {% for verb, info in verbs|dictsort(true) %}
    {{ verb|upper }}_RESPONSE_SCHEMA = {{ info.response_schema }}
    {% endfor %}
    {% for verb, info in verbs|dictsort(true) if info.body %}
    {{ verb|upper }}_BODY_SCHEMA = {{ info.body.schema }}
    {% endfor %}

    {% for verb, info in verbs|dictsort(true) %}
    async def {{ verb }}(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A {{ class_name }} instance
        """
        try:
            {% for ra in info.required_args %}
            # {{ ra.name }}: {{ ra.type }} {{ ra.description }}
            {% if ra.in == "path" %}
            {{ ra.name }} = self.request.match_info["{{ ra.name }}"]
            {% else %}
              {% if ra.type == "array" %}
                {% if ra.collectionFormat == "multi" %}
            {{ ra.name }} = self.request.query.getall("{{ ra.name }}", None)
                {% else %}
            {{ ra.name }} = self.request.query.get("{{ ra.name }}", None)
            if {{ ra.name }} is not None:
                {{ ra|parse_array }}
                {% endif %}
                {% if ra["items"].type == "integer" %}
                if {{ ra.name }}:
                    {{ ra.name }} = [int(e) for e in {{ ra.name }}]
                {% endif %}
              {% endif %}
            {% endif %}
            {% if ra.type == "boolean" %}
            {{ ra.name }} = ({{ ra.name }}.lower() == "true")
            {% elif ra.type == "integer" %}
            {{ ra.name }} = int({{ ra.name }})
            {% endif %}
            schema = {{ ra|clean_schema }}
            utils.validate({{ ra.name }}, schema)
            {% endfor %}
            optional_args = {}
            {% for oa in info.optional_args if oa.in == "query" %}
            # {{ oa.name }} (optional): {{ oa.type }} {{ oa.description }}
            {% if oa.type == "array" %}
            {% if oa.collectionFormat == "multi" %}
            {{ oa.name }} = self.request.query.getall("{{ oa.name }}", None)
            {% else %}
            {{ oa.name }} = self.request.query.get("{{ oa.name }}", None)
            if {{oa.name}} is not None:
                {{ oa|parse_array }}
            {% if oa["items"].type == "integer" %}
            if {{ oa.name }}:
                {{ oa.name }} = [int(e) for e in {{ oa.name }}]
            {% endif %}
            {% endif %}
            {% else %}
            {{ oa.name }} = self.request.query.get("{{ oa.name }}", None)
            {% endif %}
            if {{ oa.name }} is not None:
                {% if oa.type == "boolean" %}
                {{ oa.name }} = ({{ oa.name }}.lower() == "true")
                {% elif oa.type == "integer" %}
                {{ oa.name }} = int({{ oa.name }})
                {% endif %}
                schema = {{ oa|clean_schema }}
                utils.validate({{ oa.name }}, schema)
                optional_args["{{ oa.name }}"] = {{ oa.name }}
            {% endfor %}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))
        {% if info.body %}

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            utils.validate(body, schema=self.{{ verb|upper}}_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")
        {% endif %}
        {% if info.form_data %}

        form_data = {}
        {% for data in info.form_data %}
        {% if data.type == "file" %}
        raise NotImplementedError("File upload support not implemented for aiohttp.")
        {% else %}
        {{ data.name }} = self.request.POST.get("{{ data.name }}", None)
        {% endif %}
        {% if data.required %}
        if not {{ data.name }}:
            return Response(status=400, text="Formdata field '{{ data.name }}' required.")
        {% endif %}
        form_data["{{ data.name }}"] = {{ data.name }}

        {% endfor %}
        {% endif %}

        result = await Stubs.{{ info.operation }}(
            self.request, {% if info.body %}body, {% endif %}{% if info.form_data %}form_data, {% endif %}
            {% for ra in info.required_args %}{{ ra.name }}, {% endfor %}**optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.{{ verb|upper }}_RESPONSE_SCHEMA)

        {% if verb|lower == "delete" %}
        return HTTPNoContent()
        {% else %}
        return json_response(result{% if verb|lower == "post" and info.operation.endswith("_create") %}, status=201{% endif %}, headers=headers)
        {% endif %}
   {% if not loop.last %}

   {% endif %}
   {% endfor %}


{% endfor %}
class __SWAGGER_SPEC__(View, CorsViewMixin):
    SPEC = json.loads("""{{ specification }}""")

    async def get(self):
        """
        Override this function if further customisation to the spec is required.
        """
        # Mod spec to point to demo application
        spec = self.SPEC.copy()
        spec["basePath"] = "/"
        spec["host"] = "localhost:8000"
        # Add basic auth as a security definition
        security_definitions = spec.get("securityDefinitions", {})
        security_definitions["basic_auth"] = {"type": "basic"}
        spec["securityDefinitions"] = security_definitions
        return json_response(spec)

