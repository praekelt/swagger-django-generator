VENV=./ve
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
COVERAGE=$(VENV)/bin/coverage
FLAKE8=$(VENV)/bin/flake8
PROJECT=swagger_django_generator


.PHONY: check coverage test venv demo clean-demo

help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    up      Updates dependencies"
	@echo  "    deps    Ensure dev dependencies are installed"
	@echo  "    check	Checks that build is sane"
	@echo  "    lint	Reports pylint violations"
	@echo  "    test	Runs all tests"
	@echo  "    migrate Runs a database migration based on your local settings DB"
	@echo  "    redb	Rebuilds the dev DB"
	@echo  "    run 	Runs the devserver"

run:
	$(PYTHON) manage.py runserver 0.0.0.0:8000

check: $(FLAKE8)
	- $(FLAKE8) $(PROJECT) --exclude migrations --max-line-length=80

$(FLAKE8):
	$(PIP) install flake8

coverage: $(COVERAGE)
	$(COVERAGE) run --source=$(PROJECT) manage.py test
	$(COVERAGE) report

$(COVERAGE):
	$(PIP) install coverage

test:
	$(VENV)/bin/nosetests

$(VENV):
	virtualenv $(VENV)

ipython:
	$(PIP) install ipython

virtualenv: $(VENV)
	$(PIP) install -r requirements.txt

clean-virtualenv:
	rm -rf $(VENV)

demo:
	[ -d "demo" ] || $(VENV)/bin/django-admin startproject demo
	$(PYTHON) swagger_django_generator/generator.py tests/resources/petstore.json --output-dir demo/demo/ --module-name demo
	cp -r ui demo/

clean-demo:
	rm -rf demo
