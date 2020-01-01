FROM python:3.8-alpine

WORKDIR /app
RUN apk add git gcc musl-dev
RUN git clone https://github.com/praekelt/swagger-django-generator
#RUN python /app/swagger-django-generator/setup.py develop
RUN pip install pip==9.0.1 # https://github.com/praekelt/swagger-django-generator/issues/21
RUN pip install -r /app/swagger-django-generator/requirements.txt
RUN pip install swagger-spec-validator --upgrade
ENTRYPOINT ["python", "/app/swagger-django-generator/swagger_django_generator/generator.py"]
