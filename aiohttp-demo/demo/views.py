"""
Do not modify this file. It is generated from the Swagger specification.

"""
import importlib
import logging
import json
import jsonschema
import os
from jsonschema import ValidationError
from aiohttp.web import View, json_response, Response, HTTPNoContent
from aiohttp_cors import CorsViewMixin

import demo.schemas as schemas
import demo.utils as utils

# Set up logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

VALIDATE_RESPONSES = os.getenv("SWAGGER_API_VALIDATE_RESPONSES", False)
LOGGER.info("Swagger API response validation is {}".format(
    "on" if VALIDATE_RESPONSES else "off"
))

# Set up the stub class. If it is not explicitly configured in the settings.py
# file of the project, we default to a mocked class.
stub_class_path = os.getenv("STUBS_CLASS", "demo.stubs.MockedStubClass")
module_name, class_name = stub_class_path.rsplit(".", 1)
Module = importlib.import_module(module_name)
Stubs = getattr(Module, class_name)


def maybe_validate_result(result, schema):
    if VALIDATE_RESPONSES:
        try:
            jsonschema.validate(result, schema)
        except ValidationError as e:
            LOGGER.error(e.message)


class Pet(View, CorsViewMixin):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    PUT_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    POST_BODY_SCHEMA = schemas.Pet
    PUT_BODY_SCHEMA = schemas.Pet

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Pet instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.addPet(
            self.request, body, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Pet instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.updatePet(
            self.request, body, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class PetFindByStatus(View, CorsViewMixin):

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
                    ""
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
                        ""
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

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PetFindByStatus instance
        """
        try:
            optional_args = {}
            # status (optional): array Status values that need to be considered for filter
            status = self.request.query.getall("status", None)
            if status is not None:
                schema = {'collectionFormat': 'multi', 'required': False, 'type': 'array', 'description': 'Status values that need to be considered for filter', 'name': 'status', 'in': 'query', 'items': {'enum': ['available', 'pending', 'sold'], 'type': 'string'}, 'default': 'available'}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(status, schema)
                optional_args["status"] = status
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.findPetsByStatus(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class PetFindByTags(View, CorsViewMixin):

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
                    ""
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
                        ""
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

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PetFindByTags instance
        """
        try:
            optional_args = {}
            # tags (optional): array Tags to filter by
            tags = self.request.query.getall("tags", None)
            if tags is not None:
                schema = {'collectionFormat': 'multi', 'name': 'tags', 'in': 'query', 'items': {'type': 'string'}, 'type': 'array', 'description': 'Tags to filter by', 'required': False}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(tags, schema)
                optional_args["tags"] = tags
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.findPetsByTags(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class PetPetId(View, CorsViewMixin):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.Pet
    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PetPetId instance
        """
        try:
            # petId: integer Pet id to delete
            petId = self.request.match_info["petId"]
            petId = int(petId)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.deletePet(
            self.request, petId, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PetPetId instance
        """
        try:
            # petId: integer ID of pet that needs to be fetched
            petId = self.request.match_info["petId"]
            petId = int(petId)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.getPetById(
            self.request, petId, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PetPetId instance
        """
        try:
            # petId: string ID of pet that needs to be updated
            petId = self.request.match_info["petId"]
            jsonschema.validate(petId, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        form_data = {}
        name = self.request.POST.get("name", None)
        form_data["name"] = name

        status = self.request.POST.get("status", None)
        form_data["status"] = status


        result = await Stubs.updatePetWithForm(
            self.request, form_data, petId, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class PetPetIdUploadImage(View, CorsViewMixin):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PetPetIdUploadImage instance
        """
        try:
            # petId: integer ID of pet to update
            petId = self.request.match_info["petId"]
            petId = int(petId)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        form_data = {}
        additionalMetadata = self.request.POST.get("additionalMetadata", None)
        form_data["additionalMetadata"] = additionalMetadata

        raise NotImplementedError("File upload support not implemented for aiohttp.")
        form_data["file"] = file


        result = await Stubs.uploadFile(
            self.request, form_data, petId, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class StoreInventory(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "additionalProperties": {
        "format": "int32",
        "type": "integer"
    },
    "type": "object"
}""")

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A StoreInventory instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.getInventory(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class StoreOrder(View, CorsViewMixin):

    POST_RESPONSE_SCHEMA = schemas.Order
    POST_BODY_SCHEMA = schemas.Order

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A StoreOrder instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.placeOrder(
            self.request, body, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class StoreOrderOrderId(View, CorsViewMixin):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.Order

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A StoreOrderOrderId instance
        """
        try:
            # orderId: string ID of the order that needs to be deleted
            orderId = self.request.match_info["orderId"]
            jsonschema.validate(orderId, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.deleteOrder(
            self.request, orderId, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A StoreOrderOrderId instance
        """
        try:
            # orderId: string ID of pet that needs to be fetched
            orderId = self.request.match_info["orderId"]
            jsonschema.validate(orderId, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.getOrderById(
            self.request, orderId, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class User(View, CorsViewMixin):

    POST_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    POST_BODY_SCHEMA = schemas.User

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A User instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.createUser(
            self.request, body, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class UserCreateWithArray(View, CorsViewMixin):

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

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserCreateWithArray instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.createUsersWithArrayInput(
            self.request, body, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class UserCreateWithList(View, CorsViewMixin):

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

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserCreateWithList instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.createUsersWithListInput(
            self.request, body, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class UserLogin(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "type": "string"
}""")

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserLogin instance
        """
        try:
            optional_args = {}
            # username (optional): string The user name for login
            username = self.request.query.get("username", None)
            if username is not None:
                jsonschema.validate(username, {"type": "string"})
                optional_args["username"] = username
            # password (optional): string The password for login in clear text
            password = self.request.query.get("password", None)
            if password is not None:
                jsonschema.validate(password, {"type": "string"})
                optional_args["password"] = password
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.loginUser(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class UserLogout(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserLogout instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.logoutUser(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class UserUsername(View, CorsViewMixin):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.User
    PUT_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    PUT_BODY_SCHEMA = schemas.User

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserUsername instance
        """
        try:
            # username: string The name that needs to be deleted
            username = self.request.match_info["username"]
            jsonschema.validate(username, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.deleteUser(
            self.request, username, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserUsername instance
        """
        try:
            # username: string The name that needs to be fetched. Use user1 for testing. 
            username = self.request.match_info["username"]
            jsonschema.validate(username, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.getUserByName(
            self.request, username, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserUsername instance
        """
        try:
            # username: string name that need to be deleted
            username = self.request.match_info["username"]
            jsonschema.validate(username, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.updateUser(
            self.request, body, username, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class __SWAGGER_SPEC__(View, CorsViewMixin):
    SPEC = json.loads("""{
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
                        ""
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
                            ""
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

    async def get(self):
        """
        Override this function if further customisation to the spec is required.
        """
        # Mod spec to point to demo application
        spec = self.SPEC.copy()
        spec["basePath"] = "/"
        spec["host"] = "localhost:8000"
        # Add basic auth as a security definition
        security_definitions = spec.get("securityDefinitions", {})
        security_definitions["basic_auth"] = {"type": "basic"}
        spec["securityDefinitions"] = security_definitions
        return json_response(spec)
