"""
Do not modify this file. It is generated from the Swagger specification.

If you need to tweak the functionality in this file, you can replace it
with your own.
"""
from functools import wraps
import base64
import json
import jsonschema
import logging
import os
import sys
import uuid

from django.contrib.auth import authenticate, login
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from django.conf import settings


_LOGGER = logging.getLogger(__name__)


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
        return data
    except Exception as e:
        # The SuspiciousOperation exception will result in an
        # HttpResponseBadRequest response.
        raise SuspiciousOperation(e)


def login_required_no_redirect(view_func):
    """
    Helper function that returns an HTTP 401 response if the user making the
    request is not logged in, or did not provide basic HTTP authentication in
    the request.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)

        if "HTTP_AUTHORIZATION" in request.META:
            auth = request.META["HTTP_AUTHORIZATION"].split()
            if len(auth) == 2:
                # NOTE: We only support basic authentication for now.
                if auth[0].lower() == "basic":
                    base_val = base64.b64decode(auth[1])
                    if sys.version_info[0] > 2:
                        uname, passwd = base_val.split(b":")
                    else:
                        uname, passwd = base_val.split(":")
                    user = authenticate(username=uname, password=passwd)
                    if user and user.is_active:
                        login(request, user)
                        request.user = user
                        return view_func(request, *args, **kwargs)

        if "HTTP_X_API_KEY" in request.META:
            key = request.META["HTTP_X_API_KEY"]
            if key in settings.ALLOWED_API_KEYS:
                return view_func(request, *args, **kwargs)

        return HttpResponse("Unauthorized", status=401)

    return wrapper


@jsonschema.FormatChecker.cls_checks("uuid")
def check_uuid_format(instance):
    try:
        uuid.UUID(instance)
        return True
    except ValueError:
        return False


# The instance of the format checker must be created after
# the UUID format checker was registered.
_FORMAT_CHECKER = jsonschema.FormatChecker()

# Be explicit about which formats are supported. More information can be found here:
# http://python-jsonschema.readthedocs.io/en/stable/validate/#jsonschema.FormatChecker
_LOGGER.info("The following formats will be validated: {}".format(
             ", ".join(_FORMAT_CHECKER.checkers.keys())))


def validate(instance, schema):
    jsonschema.validate(instance, schema=schema,
                        format_checker=_FORMAT_CHECKER)