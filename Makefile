VENV=./ve
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
PROJECT=swagger_django_generator


.PHONY: check test virtualenv demo clean-demo

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
