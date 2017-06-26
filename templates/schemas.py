"""
Do not modify this file. It is generated from the Swagger specification.

Container module for JSONSchema definitions.
This does not include inlined definitions.

The pretty-printing functionality provided by the json module is superior to
what is provided by pformat, hence the use of json.loads().
"""
import json

{% for name, definition in schemas|dictsort(true) %}
{{ name }} = json.loads("""
{{ definition }}
""")

{% endfor %}
