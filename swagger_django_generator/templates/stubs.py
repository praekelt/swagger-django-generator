"""
This file is was generated from the Swagger specification, but may have been
updated with implementation specific code.
Use a tool like meld to pull in new definitions as opposed to overwriting
this file.
"""
import json
from apitools.datagenerator import DataGenerator

import {{ module }}.schemas as schemas


class AbstractStubClass(object):
    """
    Implementations need to be derived from this class.
    """
{% for class_name, verbs in classes|dictsort(true) %}
    {% for verb, info in verbs|dictsort(true) %}

    @staticmethod
    def {{ info.operation }}(request, {% if info.body %}body, {% endif %}{% for ra in info.required_args %}{{ ra.name }}, {% endfor %}{% for oa in info.optional_args %}{{ oa.name }}=None, {% endfor %}*args, **kwargs):
        """
        :param request: An HttpRequest
        {% for ra in info.required_args %}
        :param {{ ra.name }}: {{ ra.type }} {{ ra.description }}
        {% endfor %}
        {% for ra in info.option_args %}
        :param {{ ra.name }} (optional): {{ ra.type }} {{ ra.description }}
        {% endfor %}
        """
        raise NotImplementedError()
   {% endfor %}
{% endfor %}


class MockedStubClass(AbstractStubClass):
    """
    Provides a mocked implementation of the AbstractStubClass.
    """
    GENERATOR = DataGenerator()
{% for class_name, verbs in classes|dictsort(true) %}
    {% for verb, info in verbs|dictsort(true) %}

    @staticmethod
    def {{ info.operation }}(request, {% if info.body %}body, {% endif %}{% for ra in info.required_args %}{{ ra.name }}, {% endfor %}{% for oa in info.optional_args %}{{ oa.name }}=None, {% endfor %}*args, **kwargs):
        """
        :param request: An HttpRequest
        {% for ra in info.required_args %}
        :param {{ ra.name }}: {{ ra.type }} {{ ra.description }}
        {% endfor %}
        {% for ra in info.option_args %}
        :param {{ ra.name }} (optional): {{ ra.type }} {{ ra.description }}
        {% endfor %}
        """
        response_schema = {{ info.response_schema }}
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)
    {% endfor %}
{% endfor %}
