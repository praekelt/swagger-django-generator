"""
Do not modify this file. It is generated from the Swagger specification.

"""
import json
import jsonschema

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View

import {{ module }}.stubs as stubs
import {{ module }}.schemas as schemas


{% for class_name, verbs in classes|dictsort(true) %}
class {{ class_name }}(View):

    {% for verb, info in verbs|dictsort(true) %}
    {% if verb in ["post", "put"] %}
    @csrf_exempt
    {% endif %}
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
        body = json.loads(request.body)
        jsonschema.validate(body, {{ info.body.schema }})
        {% endif %}
        result = stubs.{{ info.operation }}(request, {% if info.body %}body, {% endif %}{% for ra in info.required_args %}{{ ra.name }}, {% endfor %}{% for oa in info.optional_args %}{{ oa.name }}=None, {% endfor %}*args, **kwargs)
        return JsonResponse(result, safe=False)
   {% if not loop.last %}

   {% endif %}
   {% endfor %}


{% endfor %}
