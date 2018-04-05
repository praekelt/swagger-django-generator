[![Build Status](https://travis-ci.org/praekelt/swagger-django-generator.svg?branch=master)](https://travis-ci.org/praekelt/swagger-django-generator)

# swagger-(django)-generator
Convert Swagger specifications into Django or aiohttp server code

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Introduction](#introduction)
- [Getting started](#getting-started)
- [Examples](#examples)
  - [A demo application](#a-demo-application)
  - [Generated files](#generated-files)
- [Notes](#notes)
- [Todo](#todo)
- [Why?](#why)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction
This utility parses a Swagger specification and generates Django- or aiohttp-specific definitions, which allows for easy integration into Django projects or creating aiohttp daemons.
In particular, the following files are currently generated:
* `urls.py`, for routing requests,
* `views.py`, for handling requests, performing validation, etc.,
* `schemas.py`, containing the JSONSchema definitions of parameters and
  request body arguments,
* `utils.py`, containing utility functions that can be tweaked, if necessary, and
* `stubs.py`, containing the abstract base class for the API functions, as well as a class containing mocked implementations of the functions.

## Getting started
A virtual environment can be set up by running
```
make virtualenv
./ve/bin/python manage.py develop  # Installs package so that templates can be found
```
This utility is self-documenting. To get an idea of what is supported, simply
run the utility with the `--help` flag:
```
└─▪ ./ve/bin/python swagger_django_generator/generator.py --help
Usage: generator.py [OPTIONS] SPECIFICATION

Options:
  --spec-format [json|yaml]
  --backend [django|aiohttp|aor]
  --verbose / --no-verbose
  --output-dir DIRECTORY
  --module-name TEXT         The name of the module where the generated code
                             will be used, e.g. myproject.some_application
  --urls-file TEXT           Use an alternative filename for the urls.
  --views-file TEXT          Use an alternative filename for the views.
  --schemas-file TEXT        Use an alternative filename for the schemas.
  --utils-file TEXT          Use an alternative filename for the utilities.
  --stubs-file TEXT          Use an alternative filename for the utilities.
  --help                     Show this message and exit.
```

By default the generated `views.py` will call a generated mock implementation, which is defined in `stubs.py` along with the abstract base class. You have create your own class derived from `AbstractStubClass`. Typically you can define this class in a file called `implementation.py` and then edit your `settings.py` to contain the following definition:
```
STUBS_CLASS = "myproject.implementation.Implementation"
```
The code generated for `aiohttp` uses a `STUBS_CLASS` environment variable.

## Admin On Rest Client Generation
The Admin on Rest portion of work is to generate a basic working Admin on Rest client that can be modified for custom requirements.
In order for the generation to behave as desired, the swagger specification is required to follow a certain configuration. Note, this generated code
comes along with a generic swagger rest server and authentication implementation.

### Path Configuration
Here is a configuration of paths for a single model to be implemented on the Admin on Rest interface.

```
"/pets": {
  "get": {
    "operationId": "pet_list",
    "parameters": [
      {
        "description": "An Optional Filter by pet_id.",
        "in": "query",
        "name": "pet_id",
        "required": false,
        "type": "integer"
      }
    ],
    "produces": [
      "application/json"
    ],
    "responses": {
      "200": {
        "description": "",
        "schema": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/pet"
          }
        }
      }
    },
    "tags": []
  },
  "post": {
    "consumes": [
      "application/json"
    ],
    "operationId": "pet_create",
    "parameters": [
      {
        "in": "body",
        "name": "data",
        "schema": {
          "$ref": "#/definitions/pet_create"
        }
      }
    ],
    "produces": [
      "application/json"
    ],
    "responses": {
      "201": {
        "description": "",
        "schema": {
          "$ref": "#/definitions/pet"
        }
      }
    },
    "tags": []
  }
},
"/pets/{pet_id}": {
  "parameters": [
    {
      "$ref": "#/parameters/pet_id"
    }
  ],
  "delete": {
    "operationId": "pet_delete",
    "responses": {
      "204": {
        "description": ""
      }
    },
    "tags": []
  },
  "get": {
    "operationId": "pet_read",
    "produces": [
      "application/json"
    ],
    "responses": {
      "200": {
        "description": "",
        "schema": {
          "$ref": "#/definitions/pet"
        }
      }
    },
    "tags": []
  },
  "put": {
    "consumes": [
      "application/json"
    ],
    "operationId": "pet_update",
    "parameters": [
      {
        "in": "body",
        "name": "data",
        "schema": {
          "$ref": "#/definitions/pet_update"
        }
      }
    ],
    "produces": [
      "application/json"
    ],
    "responses": {
      "200": {
        "description": "",
        "schema": {
          "$ref": "#/definitions/pet"
        }
      }
    },
    "tags": []
  }
}
```

This is a suitable layout for the endpoints of the Pet Model. The important attributes of each path/method pair are:

1. The base resource name `pets` remains the same for each path regarding pets. (VERY IMPORTANT)
2. With each operationId, the start is always the model name (`pet`) and the trailing word describes which AOR component the generator is looking at to generate.

All components for pets will be generated for the base resource path name `pets`, and each trailing word correlates to a given AOR component as listed below:
```
list - List Component
create - Create Component
read - Show Component
update - Edit Component
```

Here we can go over the endpoints and how they will be used in generation.

`/pets GET`: This path method will be used for the List component of the Pet model. The operationId must contain the suffix
             "list". Here the generator will build a List component for Pet based on the definition or schema provided in the 200 response for a SINGLE item of the array.
             In this example it will look at `"$ref": "#/definitions/pet"`

`/pets POST`: This path method will be used for the Create component of the Pet Model. The operationId must contain the suffix "create". Here the
              generator will build a Create component for Pet based on the definition or schema provided in the body parameter. In this example it will look at `"$ref": "#/definitions/pet_create"`.

`/pets/{pet_id} GET`: This path method will be used for the Show component of the Pet Model. The operationId must contain the suffix "read". Here the generator
                      will build a Show component for the Pet based on the definition or schema provided in the 200 response. In this example it will look at `"$ref": "#/definitions/pet"`.

`/pets/{pet_id} PUT`: This path method will be used for the Edit component of the Pet Model. The operationId must contain the suffix "update". Here the generator will
                      build an Edit component for the Pet based on the definition or schema provided in the body parameter. In this example it will look at `"$ref": "#/definitions/pet_create"`.

The delete method is not used as a standard delete component is used in the generated Admin on Rest client.

### Definition Configuration

A simple definition can be given as follows:

```
"pet": {
  "properties": {
    "id": {
      "type": "integer",
      "format": "int64",
      "readOnly": true
    },
    "category_id": {
      "type": "integer"
    },
    "name": {
      "type": "string",
      "example": "doggie"
    },
    "metadata": {
      "type": "object"
    },
    "date_of_birth": {
      "type": string
      "format": date
    },
    "created_at": {
      "type": string,
      "format": date-time
    },
    "updated_at": {
      "type": string,
      "format": date-time
    }
  }
}
```

Each property will be catered for in the generated Admin on Rest client. The property type will dictate the component to be generated for the property, however note that if the format is a supported component, it will overwrite the type component with the given format component. Also note the presence of `enum` in a property will change the component. The following types/formats have supported admin on rest components and are shown in the table below.

*NOTE: Date-time formats will require an additional npm package `aor-datetime-input` for DateTimeInput components, so add it to your project if necessary.*

| Type/Format   | Field Component  | Input Component  |
| ------------- |------------------| -----------------|
| string        | TextField        | TextInput        |
| integer       | NumberField      | NumberInput      |
| boolean       | BooleanField     | BooleanInput     |
| date          | DateField        | DateInput        |
| date-time     | DateField        | DateTimeInput    |
| enum          | SelectField      | SelectInput      |
| object*       | ObjectField*     | LongTextInput*   |

* Object types use a Custom ObjectField included in the generation of the Admin on Rest Client. For their input a LongTextInput is utilized with `parse` and `format` props that handle the sending and presentation of the field data.

### Foriegn Key relationships

Foriegn key relationships can be setup in the definition quite easily. In order for a field to be picked up as a foreign key either of the following must be present.

1. The field name is suffixed by `_id`.
2. There is an additional field for related information named `x-related-info`

The latter will appear as such:

```
"category_id": {
  "type": "integer"
  "x-related-info": {
    "model": "category", # The name of the model that is the foreign key.
    "rest_resource_name": "categories" # The base resource path on the API ie `pets` in the above path specification.
    "field": "id", # The related field of the related model.
    "label": "name" # The field to be seen when viewing the related model instance on the given model.
  }
}
```

The property will then generate a simple Reference component. Each one of the fields in the `x-related-info` attribute is optional and if not present, assumptions will be made by the generator.
The behaviour of the generator with regards to the `x-related-info` is as follows:

1. If `model` is NOT present, grab the substring before the last `_` in the property key, eg. `category`.
2. If `rest_resource_name` is NOT present, take the `model` (or the substring before the last `_` in the property key) and attempt to remove all `_` and pluralize it for a guessed base resource path on the API.
3. If `field` is NOT present, grab the substring after the last `_` in the property key, eg. `id`.
4. If `label` is NOT present, use the `field` or what was found in part 3 before.

The relation Field component will be generated as follows:

```
<ReferenceField label="Category" source="category_id" reference="categories" linkType="show" allowEmpty>
  <NumberField source="name" />
</ReferenceField>
```

The relation Input component will be generated as follows:

```
<ReferenceInput label="Category" source="category_id" reference="categories" allowEmpty>
  <SelectInput source="id" optionText="name" />
</ReferenceInput>
```

*NOTE: If you have a property with `_id` on the end and you do not want it to be a relation, set the `x-related-info` `model` field to `None`*

### Inline models

Additional info can be included in the swagger specification, at a global level, to produce inline displays on any desired model with related models. The additional field `x-detail-page-definitions` must be included on the highest level in the swagger specification with all models with inlines. An example is given as follows:

```
"x-detail-page-definitions": {
  "category": {
    "inlines": [
      {
        "model": "pet",
        "rest_resource_name": "pets",
        "label": "Pets",
        "key": "category_id",
        "fields": [
          "name",
          "date_of_birth"
        ]
      }
    ]
  }
}
```

Here we have the category model with an inline of all pets with the category_id of the given category. The optional fields here are `rest_resource_name`, `label` and `fields`.
The generator with behave as follows:

1. The `model` is required.
2. `rest_resource_name` is the base resource path to point to, and behaves the same as before. If not present, the generator will attempt to guess the base resource path with the given model name minus `_` and pluralized as best as possible.'
3. The `label` is used for aesthetic purposes.
4. The `key` is the required related_field to filter the given resource by (eg `category_id`).
5. `fields` specifies the fields to be shown in the inline, if `fields` is omitted, then all fields of the related model will be shown.

This will finally generate a `<ReferenceManyField>` with a list of all the related items.

*NOTE: The inlines will only be generated on the `Show` and `Edit` components. The Edit inlines will include edit buttons on the right side of an entry.*

### List Filters

List filters are all generated in and additional file `Filters.js`. In order to generate filters, the path in charge of dictating the list component must contain optional query parameters. These will be noticed by the generator and added to the list components filter props. Taking from the `pet` specification established above we have:

```
"get": {
  "operationId": "pet_list",
  "parameters": [
    {
      "description": "An Optional Filter by pet_id.",
      "in": "query",
      "name": "pet_id",
      "required": false,
      "type": "integer"
    }
  ],
  "produces": [
    "application/json"
  ],
  "responses": {
    "200": {
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/definitions/pet"
        }
      }
    }
  },
  "tags": []
}
```

Here we have one parameter named `pet_id`. This parameter is given `in` the `query`. This will generate a filter component for Pet list with a single filter option, many can be added to the parameters for more filter options.
The filter `type`/`format` is important for the component to be used and maps to the table as given above in the `Definition Configuration` section.

## Examples

### A demo application
For a quick demonstration of how to get started, run `make demo`. This will create a demo Django application that uses files generated by this application. The command does the following in the back:
```bash
# Create a new Django project
./ve/bin/django-admin startproject demo
# Generate files for the petstore API (including stubs) straight into the project
./ve/bin/python swagger_django_generator/generator.py tests/resources/petstore.json --output-dir demo/demo/ --module-name demo
```
You can then start the server:
```
./ve/bin/python demo/manage.py runserver
```

### Generated files

The following links references files that were generated using this utility based on the popular `PetStore` Swagger definition.

* the [schemas](generated/schemas.py) file contains global schema definitions
* the [stubs](generated/stubs.py) file is where the abstract base class for your code will live, along with a mocked implementation
* the [urls](generated/urls.py) file is where the routing takes place
* the [utils](generated/utils.py) file contains utility functions
* the [views](generated/views.py) handles security and validation
* the [stubs](generated/stubs.py) contains the abstract base class with the API functions, as well as a class containing mocked implentations.

## Notes
* All generated API calls are CSRF exempt (Django backend)
* API calls that have any form of security defined on them will require a logged in user or basic HTTP auth (Django backend)
* At this stage there are **limited tests**.

## Todo
* We can look at using the `swagger-tester` library.
* Investigate using [warlock](https://github.com/bcwaldon/warlock) or [python-jsonschema-objects](https://github.com/cwacek/python-jsonschema-objects) to generate models for ease of use.
* Look at using some of the Python libs [here](https://swagger.io/open-source-integrations/)

## Why?
Using the [Swagger/OpenAPI](https://swagger.io/) specification enables the use of a tremendous amount of tooling:

* the generation of documentation
* creating a UI to play around with the API
* [importing into Runscope](https://blog.runscope.com/posts/new-import-feature-support-for-swagger-postman) for automated test creation
* client code generation for various languages
* server code generation for various application servers

When we have to write applications that provide APIs, it will typically have to form part of a Django application. Unfortunately the "official" code generation tool only supports code generation for Tornado and Flask when it comes to the Python language.

This tool is intended to plug the gap for Django. We can focus on getting the spec right, quickly generate server code and integrate with testing frameworks like Runscope. The generated code takes care of the routing, input and output validation and common error handling.

At a minimum it allows us to get some working code up and running in very little time.
