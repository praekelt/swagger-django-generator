"""
Do not modify this file. It is generated from the Swagger specification.

"""
import importlib
import logging
import json
from jsonschema import ValidationError

from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

import {{ module }}.schemas as schemas
import {{ module }}.utils as utils

# Set up logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

try:
    VALIDATE_RESPONSES = settings.SWAGGER_API_VALIDATE_RESPONSES
except AttributeError:
    VALIDATE_RESPONSES = False
LOGGER.info("Swagger API response validation is {}".format(
    "on" if VALIDATE_RESPONSES else "off"
))

# Set up the stub class. If it is not explicitly configured in the settings.py
# file of the project, we default to a mocked class.
try:
    stub_class_path = settings.STUBS_CLASS
except AttributeError:
    stub_class_path = "{{ module }}.stubs.MockedStubClass"

module_name, class_name = stub_class_path.rsplit(".", 1)
Module = importlib.import_module(module_name)
Stubs = getattr(Module, class_name)


def maybe_validate_result(result_string, schema):
    if VALIDATE_RESPONSES:
        try:
            utils.validate(json.loads(result_string, encoding="utf8"), schema)
        except ValidationError as e:
            LOGGER.error(e.message)


{% for class_name, verbs in classes|dictsort(true) %}
@method_decorator(csrf_exempt, name="dispatch")
{% for verb, info in verbs|dictsort(true) %}
{% if info.secure %}
@method_decorator(utils.login_required_no_redirect, name="{{ verb }}")
{% endif %}
{% endfor %}
class {{ class_name }}(View):

    {% for verb, info in verbs|dictsort(true) %}
    {{ verb|upper }}_RESPONSE_SCHEMA = {{ info.response_schema }}
    {% endfor %}
    {% for verb, info in verbs|dictsort(true) if info.body %}
    {{ verb|upper }}_BODY_SCHEMA = {{ info.body.schema }}
    {% endfor %}

    {% for verb, info in verbs|dictsort(true) %}
    def {{ verb }}(self, request, {% for ra in info.required_args if ra.in == "path" %}{{ ra.name }}, {% endfor %}*args, **kwargs):
        """
        :param self: A {{ class_name }} instance
        :param request: An HttpRequest
        {% for ra in info.required_args if ra.in == "path" %}
        :param {{ ra.name }}: {{ ra.type }} {{ ra.description }}
        {% endfor %}
        """
        {% if info.body %}
        body = utils.body_to_dict(request.body, self.{{ verb|upper}}_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        {% endif %}
        {% for ra in info.required_args if ra.in == "query" %}
        if "{{ ra.name }}" not in request.GET:
            return HttpResponseBadRequest("{{ ra.name }} required")

        {% if ra.type == "array" %}
        {% if ra.collectionFormat == "multi" %}
        {{ ra.name }} = request.GET.getlist("{{ ra.name }}", None)
        {% else %}
        {{ ra.name }} = request.GET.get("{{ ra.name }}", None)
        if {{ ra.name }} is not None:
        {% if ra.collectionFormat == "pipes" %}
            {{ ra.name }} = {{ ra.name }}.split("|")
        {% elif ra.collectionFormat == "tsv" %}
            {{ ra.name }} = {{ ra.name }}.split("\t")
        {% elif ra.collectionFormat == "ssv" %}
            {{ ra.name }} = {{ ra.name }}.split(" ")
        {% elif ra.collectionFormat == "csv" %}
            {{ ra.name }} = {{ ra.name }}.split(",")
        {% else %}
            {{ ra.name }} = {{ ra.name }}.split(",")
        {% endif %}
        {% endif %}
        {% else %}
        {{ ra.name }} = request.GET.get("{{ ra.name }}")
        {% endif %}

        utils.validate({{ ra.name }}, {"type": "{{ ra.type }}"})
        {% endfor %}

        {% for oa in info.optional_args if oa.in == "query" %}
        # {{ oa.name }} (optional): {{ oa.type }} {{ oa.description }}
        {% if oa.type == "array" %}
        {% if oa.collectionFormat == "multi" %}
        {{ oa.name }} = request.GET.getlist("{{ oa.name }}", None)
        {% else %}
        {{ oa.name }} = request.GET.get("{{ oa.name }}", None)
        if {{ oa.name }} is not None:
        {% if oa.collectionFormat == "pipes" %}
            {{ oa.name }} = {{ oa.name }}.split("|")
        {% elif oa.collectionFormat == "tsv" %}
            {{ oa.name }} = {{ oa.name }}.split("\t")
        {% elif oa.collectionFormat == "ssv" %}
            {{ oa.name }} = {{ oa.name }}.split(" ")
        {% elif oa.collectionFormat == "csv" %}
            {{ oa.name }} = {{ oa.name }}.split(",")
        {% else %}
            {{ oa.name }} = {{ oa.name }}.split(",")
        {% endif %}
        {% endif %}
        {% else %}
        {{ oa.name }} = request.GET.get("{{ oa.name }}", None)
        {% endif %}
        utils.validate({{ oa.name }}, {"type": "{{ oa.type }}"})
        {% endfor %}
        {% if info.form_data %}
        form_data = {}
        {% for data in info.form_data %}
        {% if data.type == "file" %}
        {{ data.name }} = request.FILES.get("{{ data.name }}", None)
        {% else %}
        {{ data.name }} = request.POST.get("{{ data.name }}", None)
        {% endif %}
        {% if data.required %}
        if not {{ data.name }}:
            return HttpResponseBadRequest("Formdata field '{{ data.name }}' required.")
        {% endif %}
        form_data["{{ data.name }}"] = {{ data.name }}

        {% endfor %}
        {% endif %}
        result = Stubs.{{ info.operation }}(request, {% if info.body %}body, {% endif %}{% if info.form_data %}form_data, {% endif %}
            {% for ra in info.required_args %}{{ ra.name }}, {% endfor %}
            {% for oa in info.optional_args if oa.in == "query" %}{{ oa.name }}, {% endfor %})

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.{{ verb|upper }}_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response
   {% if not loop.last %}

   {% endif %}
   {% endfor %}


{% endfor %}
class __SWAGGER_SPEC__(View):

    def get(self, request, *args, **kwargs):
        spec = json.loads("""{{ specification }}""")
        # Mod spec to point to demo application
        spec["basePath"] = "/"
        spec["host"] = "localhost:8000"
        # Add basic auth as a security definition
        security_definitions = spec.get("securityDefinitions", {})
        security_definitions["basic_auth"] = {"type": "basic"}
        spec["securityDefinitions"] = security_definitions
        return JsonResponse(spec)

