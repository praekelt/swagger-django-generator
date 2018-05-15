"""
Do not modify this file. It is generated from the Swagger specification.
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

    # {{ info.operation }} -- Synchronisation point for meld
    @staticmethod
    def {{ info.operation }}(request, {% if info.body %}body, {% endif %}{% if info.form_data %}form_data, {% endif %}{% for ra in info.required_args %}{{ ra.name }}, {% endfor %}{% for oa in info.optional_args %}{{ oa.name }}=None, {% endfor %}*args, **kwargs):
        """
        :param request: An HttpRequest
        {% if info.body %}
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        {% endif %}
        {% if info.form_data %}
        :param form_data: A dictionary containing form fields and their values. In the case where the form fields refer to uploaded files, the values will be instances of `django.core.files.uploadedfile.UploadedFile`
        :type form_data: dict
        {% endif %}
        {% for ra in info.required_args %}
        :param {{ ra.name }}: {{ ra.description }}
        :type {{ ra.name }}: {{ ra.type }}
        {% endfor %}
        {% for oa in info.optional_args %}
        :param {{ oa.name }}: (optional) {{ oa.description }}
        :type {{ oa.name }}: {{ oa.type }}
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
    def {{ info.operation }}(request, {% if info.body %}body, {% endif %}{% if info.form_data %}form_data, {% endif %}{% for ra in info.required_args %}{{ ra.name }}, {% endfor %}{% for oa in info.optional_args %}{{ oa.name }}=None, {% endfor %}*args, **kwargs):
        """
        :param request: An HttpRequest
        {% if info.body %}
        :param body: A dictionary containing the parsed and validated body
        :type body: dict
        {% endif %}
        {% if info.form_data %}
        :param form_data: A dictionary containing form fields and their values. In the case where the form fields refer to uploaded files, the values will be instances of `django.core.files.uploadedfile.UploadedFile`
        :type form_data: dict
        {% endif %}
        {% for ra in info.required_args %}
        :param {{ ra.name }}: {{ ra.description }}
        :type {{ ra.name }}: {{ ra.type }}
        {% endfor %}
        {% for oa in info.optional_args %}
        :param {{ oa.name }}: (optional) {{ oa.description }}
        :type {{ oa.name }}: {{ oa.type }}
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
