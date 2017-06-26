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
  --urls-file TEXT
  --views-file TEXT
  --schemas-file TEXT
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


