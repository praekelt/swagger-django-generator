"""
Do not modify this file. It is generated from the Swagger specification.

"""
import importlib
import logging
import json
import jsonschema
from jsonschema import ValidationError

from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

import demo.schemas as schemas
import demo.utils as utils

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
    stub_class_path = "demo.stubs.MockedStubClass"

module_name, class_name = stub_class_path.rsplit(".", 1)
Module = importlib.import_module(module_name)
Stubs = getattr(Module, class_name)


def maybe_validate_result(result_string, schema):
    if VALIDATE_RESPONSES:
        try:
            jsonschema.validate(json.loads(result_string, encoding="utf8"), schema)
        except ValidationError as e:
            LOGGER.error(e.message)


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(utils.login_required_no_redirect, name="post")
@method_decorator(utils.login_required_no_redirect, name="put")
class Pet(View):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    PUT_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    POST_BODY_SCHEMA = schemas.Pet
    PUT_BODY_SCHEMA = schemas.Pet

    def post(self, request, *args, **kwargs):
        """
        :param self: A Pet instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        result = Stubs.addPet(request, body, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response

    def put(self, request, *args, **kwargs):
        """
        :param self: A Pet instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.PUT_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        result = Stubs.updatePet(request, body, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.PUT_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(utils.login_required_no_redirect, name="get")
class PetFindByStatus(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "category": {
                "properties": {
                    "id": {
                        "format": "int64",
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "x-scope": [
                    "",
                    "#/definitions/Pet"
                ],
                "xml": {
                    "name": "Category"
                }
            },
            "id": {
                "format": "int64",
                "type": "integer"
            },
            "name": {
                "example": "doggie",
                "type": "string"
            },
            "photoUrls": {
                "items": {
                    "type": "string"
                },
                "type": "array",
                "xml": {
                    "name": "photoUrl",
                    "wrapped": true
                }
            },
            "status": {
                "description": "pet status in the store",
                "enum": [
                    "available",
                    "pending",
                    "sold"
                ],
                "type": "string"
            },
            "tags": {
                "items": {
                    "properties": {
                        "id": {
                            "format": "int64",
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        }
                    },
                    "x-scope": [
                        "",
                        "#/definitions/Pet"
                    ],
                    "xml": {
                        "name": "Tag"
                    }
                },
                "type": "array",
                "xml": {
                    "name": "tag",
                    "wrapped": true
                }
            }
        },
        "required": [
            "name",
            "photoUrls"
        ],
        "x-scope": [
            ""
        ],
        "xml": {
            "name": "Pet"
        }
    },
    "type": "array"
}""")

    def get(self, request, *args, **kwargs):
        """
        :param self: A PetFindByStatus instance
        :param request: An HttpRequest
        """
        # status (optional): array Status values that need to be considered for filter
        status = request.GET.getlist("status", None)
        result = Stubs.findPetsByStatus(request, status, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(utils.login_required_no_redirect, name="get")
class PetFindByTags(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "category": {
                "properties": {
                    "id": {
                        "format": "int64",
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "x-scope": [
                    "",
                    "#/definitions/Pet"
                ],
                "xml": {
                    "name": "Category"
                }
            },
            "id": {
                "format": "int64",
                "type": "integer"
            },
            "name": {
                "example": "doggie",
                "type": "string"
            },
            "photoUrls": {
                "items": {
                    "type": "string"
                },
                "type": "array",
                "xml": {
                    "name": "photoUrl",
                    "wrapped": true
                }
            },
            "status": {
                "description": "pet status in the store",
                "enum": [
                    "available",
                    "pending",
                    "sold"
                ],
                "type": "string"
            },
            "tags": {
                "items": {
                    "properties": {
                        "id": {
                            "format": "int64",
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        }
                    },
                    "x-scope": [
                        "",
                        "#/definitions/Pet"
                    ],
                    "xml": {
                        "name": "Tag"
                    }
                },
                "type": "array",
                "xml": {
                    "name": "tag",
                    "wrapped": true
                }
            }
        },
        "required": [
            "name",
            "photoUrls"
        ],
        "x-scope": [
            ""
        ],
        "xml": {
            "name": "Pet"
        }
    },
    "type": "array"
}""")

    def get(self, request, *args, **kwargs):
        """
        :param self: A PetFindByTags instance
        :param request: An HttpRequest
        """
        # tags (optional): array Tags to filter by
        tags = request.GET.getlist("tags", None)
        result = Stubs.findPetsByTags(request, tags, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(utils.login_required_no_redirect, name="delete")
@method_decorator(utils.login_required_no_redirect, name="get")
@method_decorator(utils.login_required_no_redirect, name="post")
class PetPetId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.Pet
    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    def delete(self, request, petId, *args, **kwargs):
        """
        :param self: A PetPetId instance
        :param request: An HttpRequest
        :param petId: integer Pet id to delete
        """


        result = Stubs.deletePet(request, petId, api_key, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.DELETE_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response

    def get(self, request, petId, *args, **kwargs):
        """
        :param self: A PetPetId instance
        :param request: An HttpRequest
        :param petId: integer ID of pet that needs to be fetched
        """


        result = Stubs.getPetById(request, petId, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response

    def post(self, request, petId, *args, **kwargs):
        """
        :param self: A PetPetId instance
        :param request: An HttpRequest
        :param petId: string ID of pet that needs to be updated
        """


        form_data = {}
        name = request.POST.get("name", None)
        form_data["name"] = name

        status = request.POST.get("status", None)
        form_data["status"] = status

        result = Stubs.updatePetWithForm(request, form_data, petId, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(utils.login_required_no_redirect, name="post")
class PetPetIdUploadImage(View):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    def post(self, request, petId, *args, **kwargs):
        """
        :param self: A PetPetIdUploadImage instance
        :param request: An HttpRequest
        :param petId: integer ID of pet to update
        """


        form_data = {}
        additionalMetadata = request.POST.get("additionalMetadata", None)
        form_data["additionalMetadata"] = additionalMetadata

        file = request.FILES.get("file", None)
        form_data["file"] = file

        result = Stubs.uploadFile(request, form_data, petId, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(utils.login_required_no_redirect, name="get")
class StoreInventory(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "additionalProperties": {
        "format": "int32",
        "type": "integer"
    },
    "type": "object"
}""")

    def get(self, request, *args, **kwargs):
        """
        :param self: A StoreInventory instance
        :param request: An HttpRequest
        """
        result = Stubs.getInventory(request, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
class StoreOrder(View):

    POST_RESPONSE_SCHEMA = schemas.Order
    POST_BODY_SCHEMA = schemas.Order

    def post(self, request, *args, **kwargs):
        """
        :param self: A StoreOrder instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        result = Stubs.placeOrder(request, body, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
class StoreOrderOrderId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.Order

    def delete(self, request, orderId, *args, **kwargs):
        """
        :param self: A StoreOrderOrderId instance
        :param request: An HttpRequest
        :param orderId: string ID of the order that needs to be deleted
        """


        result = Stubs.deleteOrder(request, orderId, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.DELETE_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response

    def get(self, request, orderId, *args, **kwargs):
        """
        :param self: A StoreOrderOrderId instance
        :param request: An HttpRequest
        :param orderId: string ID of pet that needs to be fetched
        """


        result = Stubs.getOrderById(request, orderId, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
class User(View):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    POST_BODY_SCHEMA = schemas.User

    def post(self, request, *args, **kwargs):
        """
        :param self: A User instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        result = Stubs.createUser(request, body, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateWithArray(View):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    POST_BODY_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "email": {
                "type": "string"
            },
            "firstName": {
                "type": "string"
            },
            "id": {
                "format": "int64",
                "type": "integer"
            },
            "lastName": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "phone": {
                "type": "string"
            },
            "userStatus": {
                "description": "User Status",
                "format": "int32",
                "type": "integer"
            },
            "username": {
                "type": "string"
            }
        },
        "x-scope": [
            ""
        ],
        "xml": {
            "name": "User"
        }
    },
    "type": "array"
}""")

    def post(self, request, *args, **kwargs):
        """
        :param self: A UserCreateWithArray instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        result = Stubs.createUsersWithArrayInput(request, body, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateWithList(View):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    POST_BODY_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "email": {
                "type": "string"
            },
            "firstName": {
                "type": "string"
            },
            "id": {
                "format": "int64",
                "type": "integer"
            },
            "lastName": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "phone": {
                "type": "string"
            },
            "userStatus": {
                "description": "User Status",
                "format": "int32",
                "type": "integer"
            },
            "username": {
                "type": "string"
            }
        },
        "x-scope": [
            ""
        ],
        "xml": {
            "name": "User"
        }
    },
    "type": "array"
}""")

    def post(self, request, *args, **kwargs):
        """
        :param self: A UserCreateWithList instance
        :param request: An HttpRequest
        """
        body = utils.body_to_dict(request.body, self.POST_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

        result = Stubs.createUsersWithListInput(request, body, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.POST_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
class UserLogin(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "type": "string"
}""")

    def get(self, request, *args, **kwargs):
        """
        :param self: A UserLogin instance
        :param request: An HttpRequest
        """
        # username (optional): string The user name for login
        username = request.GET.get("username", None)
        # password (optional): string The password for login in clear text
        password = request.GET.get("password", None)
        result = Stubs.loginUser(request, username, password, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
class UserLogout(View):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    def get(self, request, *args, **kwargs):
        """
        :param self: A UserLogout instance
        :param request: An HttpRequest
        """
        result = Stubs.logoutUser(request, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


@method_decorator(csrf_exempt, name="dispatch")
class UserUsername(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.User
    PUT_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    PUT_BODY_SCHEMA = schemas.User

    def delete(self, request, username, *args, **kwargs):
        """
        :param self: A UserUsername instance
        :param request: An HttpRequest
        :param username: string The name that needs to be deleted
        """


        result = Stubs.deleteUser(request, username, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.DELETE_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response

    def get(self, request, username, *args, **kwargs):
        """
        :param self: A UserUsername instance
        :param request: An HttpRequest
        :param username: string The name that needs to be fetched. Use user1 for testing. 
        """


        result = Stubs.getUserByName(request, username, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response

    def put(self, request, username, *args, **kwargs):
        """
        :param self: A UserUsername instance
        :param request: An HttpRequest
        :param username: string name that need to be deleted
        """
        body = utils.body_to_dict(request.body, self.PUT_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")



        result = Stubs.updateUser(request, body, username, )

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        # The result may contain fields with date or datetime values that will not
        # pass JSON validation. We first create the response, and then maybe validate
        # the response content against the schema.
        response = JsonResponse(result, safe=False)

        maybe_validate_result(response.content, self.PUT_RESPONSE_SCHEMA)

        for key, val in headers.items():
            response[key] = val

        return response


class __SWAGGER_SPEC__(View):

    def get(self, request, *args, **kwargs):
        spec = json.loads("""{
    "basePath": "/v2",
    "definitions": {
        "Category": {
            "properties": {
                "id": {
                    "format": "int64",
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            },
            "xml": {
                "name": "Category"
            }
        },
        "Order": {
            "properties": {
                "complete": {
                    "type": "boolean"
                },
                "id": {
                    "format": "int64",
                    "type": "integer"
                },
                "petId": {
                    "format": "int64",
                    "type": "integer"
                },
                "quantity": {
                    "format": "int32",
                    "type": "integer"
                },
                "shipDate": {
                    "format": "date-time",
                    "type": "string"
                },
                "status": {
                    "description": "Order Status",
                    "enum": [
                        "placed",
                        "approved",
                        "delivered"
                    ],
                    "type": "string"
                }
            },
            "xml": {
                "name": "Order"
            }
        },
        "Pet": {
            "properties": {
                "category": {
                    "properties": {
                        "id": {
                            "format": "int64",
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        }
                    },
                    "x-scope": [
                        "",
                        "#/definitions/Pet"
                    ],
                    "xml": {
                        "name": "Category"
                    }
                },
                "id": {
                    "format": "int64",
                    "type": "integer"
                },
                "name": {
                    "example": "doggie",
                    "type": "string"
                },
                "photoUrls": {
                    "items": {
                        "type": "string"
                    },
                    "type": "array",
                    "xml": {
                        "name": "photoUrl",
                        "wrapped": true
                    }
                },
                "status": {
                    "description": "pet status in the store",
                    "enum": [
                        "available",
                        "pending",
                        "sold"
                    ],
                    "type": "string"
                },
                "tags": {
                    "items": {
                        "properties": {
                            "id": {
                                "format": "int64",
                                "type": "integer"
                            },
                            "name": {
                                "type": "string"
                            }
                        },
                        "x-scope": [
                            "",
                            "#/definitions/Pet"
                        ],
                        "xml": {
                            "name": "Tag"
                        }
                    },
                    "type": "array",
                    "xml": {
                        "name": "tag",
                        "wrapped": true
                    }
                }
            },
            "required": [
                "name",
                "photoUrls"
            ],
            "xml": {
                "name": "Pet"
            }
        },
        "Tag": {
            "properties": {
                "id": {
                    "format": "int64",
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            },
            "xml": {
                "name": "Tag"
            }
        },
        "User": {
            "properties": {
                "email": {
                    "type": "string"
                },
                "firstName": {
                    "type": "string"
                },
                "id": {
                    "format": "int64",
                    "type": "integer"
                },
                "lastName": {
                    "type": "string"
                },
                "password": {
                    "type": "string"
                },
                "phone": {
                    "type": "string"
                },
                "userStatus": {
                    "description": "User Status",
                    "format": "int32",
                    "type": "integer"
                },
                "username": {
                    "type": "string"
                }
            },
            "xml": {
                "name": "User"
            }
        }
    },
    "host": "petstore.swagger.io",
    "info": {
        "contact": {
            "email": "apiteam@wordnik.com"
        },
        "description": "This is a sample server Petstore server.  You can find out more about Swagger at <a href=\\"http://swagger.io\\">http://swagger.io</a> or on irc.freenode.net, #swagger.  For this sample, you can use the api key \\"special-key\\" to test the authorization filters",
        "license": {
            "name": "Apache 2.0",
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
        },
        "termsOfService": "http://helloreverb.com/terms/",
        "title": "Swagger Petstore",
        "version": "1.0.0"
    },
    "paths": {
        "/pet": {
            "post": {
                "consumes": [
                    "application/json",
                    "application/xml"
                ],
                "description": "",
                "operationId": "addPet",
                "parameters": [
                    {
                        "description": "Pet object that needs to be added to the store",
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "$ref": "#/definitions/Pet",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "405": {
                        "description": "Invalid input"
                    }
                },
                "security": [
                    {
                        "petstore_auth": [
                            "write:pets",
                            "read:pets"
                        ]
                    }
                ],
                "summary": "Add a new pet to the store",
                "tags": [
                    "pet"
                ]
            },
            "put": {
                "consumes": [
                    "application/json",
                    "application/xml"
                ],
                "description": "",
                "operationId": "updatePet",
                "parameters": [
                    {
                        "description": "Pet object that needs to be added to the store",
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "$ref": "#/definitions/Pet",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "400": {
                        "description": "Invalid ID supplied"
                    },
                    "404": {
                        "description": "Pet not found"
                    },
                    "405": {
                        "description": "Validation exception"
                    }
                },
                "security": [
                    {
                        "petstore_auth": [
                            "write:pets",
                            "read:pets"
                        ]
                    }
                ],
                "summary": "Update an existing pet",
                "tags": [
                    "pet"
                ]
            }
        },
        "/pet/findByStatus": {
            "get": {
                "description": "Multiple status values can be provided with comma separated strings",
                "operationId": "findPetsByStatus",
                "parameters": [
                    {
                        "collectionFormat": "multi",
                        "default": "available",
                        "description": "Status values that need to be considered for filter",
                        "in": "query",
                        "items": {
                            "enum": [
                                "available",
                                "pending",
                                "sold"
                            ],
                            "type": "string"
                        },
                        "name": "status",
                        "required": false,
                        "type": "array"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "examples": {
                            "application/json": {
                                "breed": "Mixed",
                                "color": "Black",
                                "gender": "Female",
                                "name": "Puma",
                                "type": "Dog"
                            }
                        },
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/Pet",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    },
                    "400": {
                        "description": "Invalid status value"
                    }
                },
                "security": [
                    {
                        "petstore_auth": [
                            "write:pets",
                            "read:pets"
                        ]
                    }
                ],
                "summary": "Finds Pets by status",
                "tags": [
                    "pet"
                ]
            }
        },
        "/pet/findByTags": {
            "get": {
                "description": "Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.",
                "operationId": "findPetsByTags",
                "parameters": [
                    {
                        "collectionFormat": "multi",
                        "description": "Tags to filter by",
                        "in": "query",
                        "items": {
                            "type": "string"
                        },
                        "name": "tags",
                        "required": false,
                        "type": "array"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/Pet",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    },
                    "400": {
                        "description": "Invalid tag value"
                    }
                },
                "security": [
                    {
                        "petstore_auth": [
                            "write:pets",
                            "read:pets"
                        ]
                    }
                ],
                "summary": "Finds Pets by tags",
                "tags": [
                    "pet"
                ]
            }
        },
        "/pet/{petId}": {
            "delete": {
                "description": "",
                "operationId": "deletePet",
                "parameters": [
                    {
                        "description": "",
                        "in": "header",
                        "name": "api_key",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "Pet id to delete",
                        "format": "int64",
                        "in": "path",
                        "name": "petId",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "400": {
                        "description": "Invalid pet value"
                    }
                },
                "security": [
                    {
                        "petstore_auth": [
                            "write:pets",
                            "read:pets"
                        ]
                    }
                ],
                "summary": "Deletes a pet",
                "tags": [
                    "pet"
                ]
            },
            "get": {
                "description": "Returns a pet when ID < 10.  ID > 10 or nonintegers will simulate API error conditions",
                "operationId": "getPetById",
                "parameters": [
                    {
                        "description": "ID of pet that needs to be fetched",
                        "format": "int64",
                        "in": "path",
                        "name": "petId",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "$ref": "#/definitions/Pet",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "400": {
                        "description": "Invalid ID supplied"
                    },
                    "404": {
                        "description": "Pet not found"
                    }
                },
                "security": [
                    {
                        "api_key": []
                    },
                    {
                        "petstore_auth": [
                            "write:pets",
                            "read:pets"
                        ]
                    }
                ],
                "summary": "Find pet by ID",
                "tags": [
                    "pet"
                ]
            },
            "post": {
                "consumes": [
                    "application/x-www-form-urlencoded"
                ],
                "description": "",
                "operationId": "updatePetWithForm",
                "parameters": [
                    {
                        "description": "ID of pet that needs to be updated",
                        "in": "path",
                        "name": "petId",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "description": "Updated name of the pet",
                        "in": "formData",
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "Updated status of the pet",
                        "in": "formData",
                        "name": "status",
                        "required": false,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "405": {
                        "description": "Invalid input"
                    }
                },
                "security": [
                    {
                        "petstore_auth": [
                            "write:pets",
                            "read:pets"
                        ]
                    }
                ],
                "summary": "Updates a pet in the store with form data",
                "tags": [
                    "pet"
                ]
            }
        },
        "/pet/{petId}/uploadImage": {
            "post": {
                "consumes": [
                    "multipart/form-data"
                ],
                "description": "",
                "operationId": "uploadFile",
                "parameters": [
                    {
                        "description": "ID of pet to update",
                        "format": "int64",
                        "in": "path",
                        "name": "petId",
                        "required": true,
                        "type": "integer"
                    },
                    {
                        "description": "Additional data to pass to server",
                        "in": "formData",
                        "name": "additionalMetadata",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "file to upload",
                        "in": "formData",
                        "name": "file",
                        "required": false,
                        "type": "file"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "default": {
                        "description": "successful operation"
                    }
                },
                "security": [
                    {
                        "petstore_auth": [
                            "write:pets",
                            "read:pets"
                        ]
                    }
                ],
                "summary": "uploads an image",
                "tags": [
                    "pet"
                ]
            }
        },
        "/store/inventory": {
            "get": {
                "description": "Returns a map of status codes to quantities",
                "operationId": "getInventory",
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "additionalProperties": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "type": "object"
                        }
                    }
                },
                "security": [
                    {
                        "api_key": []
                    }
                ],
                "summary": "Returns pet inventories by status",
                "tags": [
                    "store"
                ]
            }
        },
        "/store/order": {
            "post": {
                "description": "",
                "operationId": "placeOrder",
                "parameters": [
                    {
                        "description": "order placed for purchasing the pet",
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "$ref": "#/definitions/Order",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "$ref": "#/definitions/Order",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "400": {
                        "description": "Invalid Order"
                    }
                },
                "summary": "Place an order for a pet",
                "tags": [
                    "store"
                ]
            }
        },
        "/store/order/{orderId}": {
            "delete": {
                "description": "For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors",
                "operationId": "deleteOrder",
                "parameters": [
                    {
                        "description": "ID of the order that needs to be deleted",
                        "in": "path",
                        "name": "orderId",
                        "required": true,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "400": {
                        "description": "Invalid ID supplied"
                    },
                    "404": {
                        "description": "Order not found"
                    }
                },
                "summary": "Delete purchase order by ID",
                "tags": [
                    "store"
                ]
            },
            "get": {
                "description": "For valid response try integer IDs with value <= 5 or > 10. Other values will generated exceptions",
                "operationId": "getOrderById",
                "parameters": [
                    {
                        "description": "ID of pet that needs to be fetched",
                        "in": "path",
                        "name": "orderId",
                        "required": true,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "$ref": "#/definitions/Order",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "400": {
                        "description": "Invalid ID supplied"
                    },
                    "404": {
                        "description": "Order not found"
                    }
                },
                "summary": "Find purchase order by ID",
                "tags": [
                    "store"
                ]
            }
        },
        "/user": {
            "post": {
                "description": "This can only be done by the logged in user.",
                "operationId": "createUser",
                "parameters": [
                    {
                        "description": "Created user object",
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "$ref": "#/definitions/User",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "default": {
                        "description": "successful operation"
                    }
                },
                "summary": "Create user",
                "tags": [
                    "user"
                ]
            }
        },
        "/user/createWithArray": {
            "post": {
                "description": "",
                "operationId": "createUsersWithArrayInput",
                "parameters": [
                    {
                        "description": "List of user object",
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/User",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "default": {
                        "description": "successful operation"
                    }
                },
                "summary": "Creates list of users with given input array",
                "tags": [
                    "user"
                ]
            }
        },
        "/user/createWithList": {
            "post": {
                "description": "",
                "operationId": "createUsersWithListInput",
                "parameters": [
                    {
                        "description": "List of user object",
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/User",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "default": {
                        "description": "successful operation"
                    }
                },
                "summary": "Creates list of users with given input array",
                "tags": [
                    "user"
                ]
            }
        },
        "/user/login": {
            "get": {
                "description": "",
                "operationId": "loginUser",
                "parameters": [
                    {
                        "description": "The user name for login",
                        "in": "query",
                        "name": "username",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "The password for login in clear text",
                        "in": "query",
                        "name": "password",
                        "required": false,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "type": "string"
                        }
                    },
                    "400": {
                        "description": "Invalid username/password supplied"
                    }
                },
                "summary": "Logs user into the system",
                "tags": [
                    "user"
                ]
            }
        },
        "/user/logout": {
            "get": {
                "description": "",
                "operationId": "logoutUser",
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "default": {
                        "description": "successful operation"
                    }
                },
                "summary": "Logs out current logged in user session",
                "tags": [
                    "user"
                ]
            }
        },
        "/user/{username}": {
            "delete": {
                "description": "This can only be done by the logged in user.",
                "operationId": "deleteUser",
                "parameters": [
                    {
                        "description": "The name that needs to be deleted",
                        "in": "path",
                        "name": "username",
                        "required": true,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "400": {
                        "description": "Invalid username supplied"
                    },
                    "404": {
                        "description": "User not found"
                    }
                },
                "summary": "Delete user",
                "tags": [
                    "user"
                ]
            },
            "get": {
                "description": "",
                "operationId": "getUserByName",
                "parameters": [
                    {
                        "description": "The name that needs to be fetched. Use user1 for testing. ",
                        "in": "path",
                        "name": "username",
                        "required": true,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "$ref": "#/definitions/User",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "400": {
                        "description": "Invalid username supplied"
                    },
                    "404": {
                        "description": "User not found"
                    }
                },
                "summary": "Get user by user name",
                "tags": [
                    "user"
                ]
            },
            "put": {
                "description": "This can only be done by the logged in user.",
                "operationId": "updateUser",
                "parameters": [
                    {
                        "description": "name that need to be deleted",
                        "in": "path",
                        "name": "username",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "description": "Updated user object",
                        "in": "body",
                        "name": "body",
                        "required": false,
                        "schema": {
                            "$ref": "#/definitions/User",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json",
                    "application/xml"
                ],
                "responses": {
                    "400": {
                        "description": "Invalid user supplied"
                    },
                    "404": {
                        "description": "User not found"
                    }
                },
                "summary": "Updated user",
                "tags": [
                    "user"
                ]
            }
        }
    },
    "schemes": [
        "http"
    ],
    "securityDefinitions": {
        "api_key": {
            "in": "header",
            "name": "api_key",
            "type": "apiKey"
        },
        "petstore_auth": {
            "authorizationUrl": "http://petstore.swagger.io/api/oauth/dialog",
            "flow": "implicit",
            "scopes": {
                "read:pets": "read your pets",
                "write:pets": "modify pets in your account"
            },
            "type": "oauth2"
        }
    },
    "swagger": "2.0"
}""")
        # Mod spec to point to demo application
        spec["basePath"] = "/"
        spec["host"] = "localhost:8000"
        # Add basic auth as a security definition
        security_definitions = spec.get("securityDefinitions", {})
        security_definitions["basic_auth"] = {"type": "basic"}
        spec["securityDefinitions"] = security_definitions
        return JsonResponse(spec)
