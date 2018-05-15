"""
Do not modify this file. It is generated from the Swagger specification.
"""
import json
from apitools.datagenerator import DataGenerator

import demo.schemas as schemas


class AbstractStubClass(object):
    """
    Implementations need to be derived from this class.
    """

    # addPet -- Synchronisation point for meld
    @staticmethod
    def addPet(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    # updatePet -- Synchronisation point for meld
    @staticmethod
    def updatePet(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    # findPetsByStatus -- Synchronisation point for meld
    @staticmethod
    def findPetsByStatus(request, status=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param status (optional): array Status values that need to be considered for filter
        """
        raise NotImplementedError()

    # findPetsByTags -- Synchronisation point for meld
    @staticmethod
    def findPetsByTags(request, tags=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param tags (optional): array Tags to filter by
        """
        raise NotImplementedError()

    # deletePet -- Synchronisation point for meld
    @staticmethod
    def deletePet(request, petId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param petId: integer Pet id to delete
        """
        raise NotImplementedError()

    # getPetById -- Synchronisation point for meld
    @staticmethod
    def getPetById(request, petId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param petId: integer ID of pet that needs to be fetched
        """
        raise NotImplementedError()

    # updatePetWithForm -- Synchronisation point for meld
    @staticmethod
    def updatePetWithForm(request, form_data, petId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param form_data: dict A dictionary containing form fields and their values. In the case where the form fields refer to uploaded files, the values will be instances of `django.core.files.uploadedfile.UploadedFile`
        :param petId: string ID of pet that needs to be updated
        """
        raise NotImplementedError()

    # uploadFile -- Synchronisation point for meld
    @staticmethod
    def uploadFile(request, form_data, petId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param form_data: dict A dictionary containing form fields and their values. In the case where the form fields refer to uploaded files, the values will be instances of `django.core.files.uploadedfile.UploadedFile`
        :param petId: integer ID of pet to update
        """
        raise NotImplementedError()

    # getInventory -- Synchronisation point for meld
    @staticmethod
    def getInventory(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        raise NotImplementedError()

    # placeOrder -- Synchronisation point for meld
    @staticmethod
    def placeOrder(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    # deleteOrder -- Synchronisation point for meld
    @staticmethod
    def deleteOrder(request, orderId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param orderId: string ID of the order that needs to be deleted
        """
        raise NotImplementedError()

    # getOrderById -- Synchronisation point for meld
    @staticmethod
    def getOrderById(request, orderId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param orderId: string ID of pet that needs to be fetched
        """
        raise NotImplementedError()

    # createUser -- Synchronisation point for meld
    @staticmethod
    def createUser(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    # createUsersWithArrayInput -- Synchronisation point for meld
    @staticmethod
    def createUsersWithArrayInput(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    # createUsersWithListInput -- Synchronisation point for meld
    @staticmethod
    def createUsersWithListInput(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    # loginUser -- Synchronisation point for meld
    @staticmethod
    def loginUser(request, username=None, password=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param username (optional): string The user name for login
        :param password (optional): string The password for login in clear text
        """
        raise NotImplementedError()

    # logoutUser -- Synchronisation point for meld
    @staticmethod
    def logoutUser(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        raise NotImplementedError()

    # deleteUser -- Synchronisation point for meld
    @staticmethod
    def deleteUser(request, username, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param username: string The name that needs to be deleted
        """
        raise NotImplementedError()

    # getUserByName -- Synchronisation point for meld
    @staticmethod
    def getUserByName(request, username, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param username: string The name that needs to be fetched. Use user1 for testing. 
        """
        raise NotImplementedError()

    # updateUser -- Synchronisation point for meld
    @staticmethod
    def updateUser(request, body, username, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param username: string name that need to be deleted
        """
        raise NotImplementedError()


class MockedStubClass(AbstractStubClass):
    """
    Provides a mocked implementation of the AbstractStubClass.
    """
    GENERATOR = DataGenerator()

    @staticmethod
    def addPet(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def updatePet(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def findPetsByStatus(request, status=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param status (optional): array Status values that need to be considered for filter
        """
        response_schema = json.loads("""{
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
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def findPetsByTags(request, tags=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param tags (optional): array Tags to filter by
        """
        response_schema = json.loads("""{
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
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def deletePet(request, petId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param petId: integer Pet id to delete
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def getPetById(request, petId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param petId: integer ID of pet that needs to be fetched
        """
        response_schema = schemas.Pet
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def updatePetWithForm(request, form_data, petId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param form_data: dict A dictionary containing form fields and their values. In the case where the form fields refer to uploaded files, the values will be instances of `django.core.files.uploadedfile.UploadedFile`
        :param petId: string ID of pet that needs to be updated
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def uploadFile(request, form_data, petId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param form_data: dict A dictionary containing form fields and their values. In the case where the form fields refer to uploaded files, the values will be instances of `django.core.files.uploadedfile.UploadedFile`
        :param petId: integer ID of pet to update
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def getInventory(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        response_schema = json.loads("""{
    "additionalProperties": {
        "format": "int32",
        "type": "integer"
    },
    "type": "object"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def placeOrder(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.Order
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def deleteOrder(request, orderId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param orderId: string ID of the order that needs to be deleted
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def getOrderById(request, orderId, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param orderId: string ID of pet that needs to be fetched
        """
        response_schema = schemas.Order
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def createUser(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def createUsersWithArrayInput(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def createUsersWithListInput(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def loginUser(request, username=None, password=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param username (optional): string The user name for login
        :param password (optional): string The password for login in clear text
        """
        response_schema = json.loads("""{
    "type": "string"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def logoutUser(request, *args, **kwargs):
        """
        :param request: An HttpRequest
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def deleteUser(request, username, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param username: string The name that needs to be deleted
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def getUserByName(request, username, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param username: string The name that needs to be fetched. Use user1 for testing. 
        """
        response_schema = schemas.User
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    def updateUser(request, body, username, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param username: string name that need to be deleted
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)
