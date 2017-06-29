"""
Do not modify this file. It is generated from the Swagger specification.

If you need to tweak the functionality in this file, you can replace it
with your own.
"""
import json
import jsonschema
from django.core.exceptions import SuspiciousOperation


def body_to_dict(body, schema):
    # type: (str, Dict) -> Dict
    """

    :param body: The body content
    :param schema: The expected JSONSchema
    :return: A dictionary containing the parsed body
    :raises SuspiciousOperation: If the body is not in JSON format, or does not
       conform to the specified schema.
    """
    try:
        data = json.loads(body)
        jsonschema.validate(data, schema=schema)
    except Exception as e:
        # The SuspiciousOperation exception will result in an
        # HttpResponseBadRequest response.
        raise SuspiciousOperation(e)
