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
    async def addPet(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # updatePet -- Synchronisation point for meld
    @staticmethod
    async def updatePet(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # findPetsByStatus -- Synchronisation point for meld
    @staticmethod
    async def findPetsByStatus(request, **kwargs):
        """
        :param request: An HttpRequest
        :param status (optional): array Status values that need to be considered for filter
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # findPetsByTags -- Synchronisation point for meld
    @staticmethod
    async def findPetsByTags(request, **kwargs):
        """
        :param request: An HttpRequest
        :param tags (optional): array Tags to filter by
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletePet -- Synchronisation point for meld
    @staticmethod
    async def deletePet(request, petId, **kwargs):
        """
        :param request: An HttpRequest
        :param petId: integer Pet id to delete
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # getPetById -- Synchronisation point for meld
    @staticmethod
    async def getPetById(request, petId, **kwargs):
        """
        :param request: An HttpRequest
        :param petId: integer ID of pet that needs to be fetched
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # updatePetWithForm -- Synchronisation point for meld
    @staticmethod
    async def updatePetWithForm(request, form_data, petId, **kwargs):
        """
        :param request: An HttpRequest
        :param form_data: dict A dictionary containing form fields and their values. In the case where the form fields refer to uploaded files, the values will be instances of `django.core.files.uploadedfile.UploadedFile`
        :param petId: string ID of pet that needs to be updated
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # uploadFile -- Synchronisation point for meld
    @staticmethod
    async def uploadFile(request, form_data, petId, **kwargs):
        """
        :param request: An HttpRequest
        :param form_data: dict A dictionary containing form fields and their values. In the case where the form fields refer to uploaded files, the values will be instances of `django.core.files.uploadedfile.UploadedFile`
        :param petId: integer ID of pet to update
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # getInventory -- Synchronisation point for meld
    @staticmethod
    async def getInventory(request, **kwargs):
        """
        :param request: An HttpRequest
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # placeOrder -- Synchronisation point for meld
    @staticmethod
    async def placeOrder(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deleteOrder -- Synchronisation point for meld
    @staticmethod
    async def deleteOrder(request, orderId, **kwargs):
        """
        :param request: An HttpRequest
        :param orderId: string ID of the order that needs to be deleted
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # getOrderById -- Synchronisation point for meld
    @staticmethod
    async def getOrderById(request, orderId, **kwargs):
        """
        :param request: An HttpRequest
        :param orderId: string ID of pet that needs to be fetched
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # createUser -- Synchronisation point for meld
    @staticmethod
    async def createUser(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # createUsersWithArrayInput -- Synchronisation point for meld
    @staticmethod
    async def createUsersWithArrayInput(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # createUsersWithListInput -- Synchronisation point for meld
    @staticmethod
    async def createUsersWithListInput(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # loginUser -- Synchronisation point for meld
    @staticmethod
    async def loginUser(request, **kwargs):
        """
        :param request: An HttpRequest
        :param username (optional): string The user name for login
        :param password (optional): string The password for login in clear text
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # logoutUser -- Synchronisation point for meld
    @staticmethod
    async def logoutUser(request, **kwargs):
        """
        :param request: An HttpRequest
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deleteUser -- Synchronisation point for meld
    @staticmethod
    async def deleteUser(request, username, **kwargs):
        """
        :param request: An HttpRequest
        :param username: string The name that needs to be deleted
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # getUserByName -- Synchronisation point for meld
    @staticmethod
    async def getUserByName(request, username, **kwargs):
        """
        :param request: An HttpRequest
        :param username: string The name that needs to be fetched. Use user1 for testing. 
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # updateUser -- Synchronisation point for meld
    @staticmethod
    async def updateUser(request, body, username, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param username: string name that need to be deleted
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()


class MockedStubClass(AbstractStubClass):
    """
    Provides a mocked implementation of the AbstractStubClass.
    """
    GENERATOR = DataGenerator()


    @staticmethod
    async def addPet(request, body, **kwargs):
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
    async def updatePet(request, body, **kwargs):
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
    async def findPetsByStatus(request, **kwargs):
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
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def findPetsByTags(request, **kwargs):
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
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deletePet(request, petId, **kwargs):
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
    async def getPetById(request, petId, **kwargs):
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
    async def updatePetWithForm(request, form_data, petId, **kwargs):
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
    async def uploadFile(request, form_data, petId, **kwargs):
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
    async def getInventory(request, **kwargs):
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
    async def placeOrder(request, body, **kwargs):
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
    async def deleteOrder(request, orderId, **kwargs):
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
    async def getOrderById(request, orderId, **kwargs):
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
    async def createUser(request, body, **kwargs):
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
    async def createUsersWithArrayInput(request, body, **kwargs):
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
    async def createUsersWithListInput(request, body, **kwargs):
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
    async def loginUser(request, **kwargs):
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
    async def logoutUser(request, **kwargs):
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
    async def deleteUser(request, username, **kwargs):
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
    async def getUserByName(request, username, **kwargs):
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
    async def updateUser(request, body, username, **kwargs):
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
