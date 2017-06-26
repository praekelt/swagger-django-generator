"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
from django.conf.urls import url
import {{ module }}.views as views

urlpatterns = [
    {% for relative_url, class_name in entries|dictsort(true) %}
    url(r"^{{ relative_url }}$", views.{{ class_name }}.as_view()),
    {% endfor %}
]
