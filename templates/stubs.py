"""
This file is was generated from the Swagger specification, but may have been
updated with implementation specific code.
Use a tool like meld to pull in new definitions as opposed to overwriting
this file.
"""
{% for class_name, verbs in classes|dictsort(true) %}
    {% for verb, info in verbs|dictsort(true) %}


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
    # TODO: Implement me
    return {}
   {% endfor %}
{% endfor %}
