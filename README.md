# swagger-django-generator
Convert Swagger specifications into Django code

## Introduction
This utility parses a Swagger specification and generates Django-specific
definitions, which allows for easy integration into Django projects.
In particular, the following files are currently generated:
* `urls.py`, for routing requests,
* `views.py`, for handling requests, performing validation, etc., and
* `schemas.py`, containing the JSONSchema definitions of parameters and
  request body arguments.

## Getting started
A virtual environment can be set up by running
```
make virtualenv
```
This utility is self-documenting. To get an idea of what is supported, simply
run the utility with the `--help` flag:
```
└─▪ ./ve/bin/python swagger_django_generator/generator.py --help
Usage: generator.py [OPTIONS] SPECIFICATION

Options:
  --verbose / --no-verbose
  --output-dir DIRECTORY
  --module-name TEXT        The name of the module where the generated code
                            will be used, e.g. myproject.some_application
  --urls-file TEXT          Use an alternative filename for the urls.
  --views-file TEXT         Use an alternative filename for the views.
  --schemas-file TEXT       Use an alternative filename for the schemas.
  --help                    Show this message and exit.
```

At the time of writing the ulity expects you to implement your logic in a `stubs.py` file.
The name of this module will be made configurable in future releases.

## Todo
* Currently `PUT` and `POST` request handlers are generated with a `@csrf_exempt` decorator.
This can be made a command line option.
* Currently the generated code expects logic to be implemented in a file called `stubs.py`. This needs to be made configurable.
* Only `yaml` defintions are currenlty parsed. It should be trivial to support JSON as well, since
it is provided by the `swagger-parser` library.
* We can look at using the `swagger-tester` library.
* At this stage there are **no tests**. This should be remedied as soon as possible.

## Examples
Here are some examples of the files that are generated.

### `urls.py`
```python
"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
from django.conf.urls import url
import generated.views as views

urlpatterns = [
    url(r"^/claims$", views.Claims.as_view()),
    url(r"^/feersum/channels/$", views.FeersumChannels.as_view()),
    url(r"^/feersum/channels/(?P<channel_id>.+)/$", views.FeersumChannelsChannelId.as_view()),
    url(r"^/feersum/channels/(?P<channel_id>.+)/messages/$", views.FeersumChannelsChannelIdMessages.as_view()),
    url(r"^/feersum/channels/(?P<channel_id>.+)/userinfo/(?P<recipient_id>.+)/$", views.FeersumChannelsChannelIdUserinfoRecipientId.as_view()),
    url(r"^/feersum/hello$", views.FeersumHello.as_view()),
    url(r"^/manufacturer/(?P<manufacturer_id>.+)/models$", views.ManufacturerManufacturerIdModels.as_view()),
    url(r"^/manufacturers$", views.Manufacturers.as_view()),
    url(r"^/models$", views.Models.as_view()),
    url(r"^/notifications$", views.Notifications.as_view()),
    url(r"^/policies$", views.Policies.as_view()),
    url(r"^/user$", views.User.as_view()),
]
```

### `schemas.py`
```python
"""
Do not modify this file. It is generated from the Swagger specification.

Container module for JSONSchema definitions.
This does not include inlined definitions.

The pretty-printing functionality provided by the json module is superior to
what is provided by pformat, hence the use of json.loads().
"""
import json

claim = json.loads("""
{
    "properties": {
        "created_date": {
            "format": "date-time",
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "id": {
            "type": "integer"
        },
        "risk_item_id": {
            "type": "integer"
        }
    },
    "type": "object"
}
""")

create_policy = json.loads("""
{
    "properties": {
        "IMEI": {
            "description": "The IMEI of the insured device",
            "pattern": "[0-9]{15, 17}",
            "type": "string"
        },
        "model_id": {
            "description": "The model ID. The manufacturer is implied.",
            "type": "integer"
        },
        "send_email": {
            "default": false,
            "description": "A flag indicating whether an email should be sent to the user",
            "type": "boolean"
        }
    },
    "type": "object"
}
""")
```

### `views.py`
```python
"""
Do not modify this file. It is generated from the Swagger specification.

"""
import json
import jsonschema

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View

import generated.stubs as stubs
import generated.schemas as schemas


class Manufacturers(View):

    def get(self, request, *args, **kwargs):
        """
        :param self: A Manufacturers instance
        :param request: An HttpRequest
        """
        result = stubs.list_manufacturers(request, *args, **kwargs)
        return JsonResponse(result, safe=False)


class FeersumChannelsChannelIdMessages(View):

    @csrf_exempt
    def post(self, request, channel_id, *args, **kwargs):
        """
        :param self: A FeersumChannelsChannelIdMessages instance
        :param request: An HttpRequest
        :param channel_id: string The channel id
        """
        body = json.loads(request.body)
        jsonschema.validate(body, schemas.message)
        result = stubs.receive_message(request, body, channel_id, *args, **kwargs)
        return JsonResponse(result, safe=False)


class Policies(View):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        """
        :param self: A Policies instance
        :param request: An HttpRequest
        """
        body = json.loads(request.body)
        jsonschema.validate(body, schemas.create_policy)
        result = stubs.createUserPolicy(request, body, *args, **kwargs)
        return JsonResponse(result, safe=False)

    def get(self, request, *args, **kwargs):
        """
        :param self: A Policies instance
        :param request: An HttpRequest
        """
        result = stubs.get_user_policies(request, *args, **kwargs)
        return JsonResponse(result, safe=False)
```
