"""
Do not modify this file. It is generated from the Swagger specification.

Container module for JSONSchema definitions.
This does not include inlined definitions.

The pretty-printing functionality provided by the json module is superior to
what is provided by pformat, hence the use of json.loads().
"""
import json

# When no schema is provided in the definition, we use an empty schema
__UNSPECIFIED__ = {}

Category = json.loads("""
{
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
}
""")

Order = json.loads("""
{
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
}
""")

Pet = json.loads("""
{
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
}
""")

Tag = json.loads("""
{
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
}
""")

User = json.loads("""
{
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
""")

