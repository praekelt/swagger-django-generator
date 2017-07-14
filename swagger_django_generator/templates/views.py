"""
Do not modify this file. It is generated from the Swagger specification.

"""
import logging
import json
import jsonschema
from jsonschema import ValidationError

from django.conf import settings
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from {{ module }}.stubs import MockedStubClass as Stubs
import {{ module }}.schemas as schemas
import {{ module }}.utils as utils


logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
try:
    VALIDATE_RESPONSES = settings.SWAGGER_API_VALIDATE_RESPONSES
except AttributeError:
    VALIDATE_RESPONSES = False
LOGGER.info("Swagger API response validation is {}".format(
    "on" if VALIDATE_RESPONSES else "off"
))


def maybe_validate_result(result, schema):
    if VALIDATE_RESPONSES:
        try:
            jsonschema.validate(result, schema)
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
    def {{ verb }}(self, request, {% for ra in info.required_args %}{{ ra.name }}, {% endfor %}{% for oa in info.optional_args %}{{ oa.name }}=None, {% endfor %}*args, **kwargs):
        """
        :param self: A {{ class_name }} instance
        :param request: An HttpRequest
        {% for ra in info.required_args %}
        :param {{ ra.name }}: {{ ra.type }} {{ ra.description }}
        {% endfor %}
        {% for ra in info.option_args %}
        :param {{ ra.name }} (optional): {{ ra.type }} {{ ra.description }}
        {% endfor %}
        """
        {% if info.body %}
        body = utils.body_to_dict(request.body, self.{{ verb|upper}}_BODY_SCHEMA)
        {% endif %}
        result = Stubs.{{ info.operation }}(request, {% if info.body %}body, {% endif %}{% for ra in info.required_args %}{{ ra.name }}, {% endfor %}{% for oa in info.optional_args %}{{ oa.name }}=None, {% endfor %}*args, **kwargs)
        maybe_validate_result(result, self.{{ verb|upper }}_RESPONSE_SCHEMA)

        return JsonResponse(result, safe=False)
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

