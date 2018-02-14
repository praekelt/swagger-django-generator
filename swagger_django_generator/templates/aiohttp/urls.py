"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
import {{ module }}.views as views

def add_routes(app):
    {# URLs are traverse in reversed sorted order so that longer ones are evaluated first #}
    {% for relative_url, class_name in entries|dictsort(true)|reverse %}
    app.router.add_view(r"/{{ relative_url }}", views.{{ class_name }})
    {% endfor %}
    # if settings.DEBUG:
    app.router.add_view(r"/the_specification", views.__SWAGGER_SPEC__)
    app.router.add_static(r"/ui", path="ui")
