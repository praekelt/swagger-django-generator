"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
import {{ module }}.views as views
import aiohttp_cors

def add_routes(app, with_ui=False):
    {# URLs are traverse in reversed sorted order so that longer ones are evaluated first #}
    {% for relative_url, class_name in entries|dictsort(true)|reverse %}
    app.router.add_view(r"/{{ relative_url }}", views.{{ class_name }})
    {% endfor %}
    if with_ui:
        app.router.add_view(r"/the_specification", views.__SWAGGER_SPEC__)
        app.router.add_static(r"/ui", path="ui")

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Configure CORS on all routes.
    for route in app.router.routes():
        cors.add(route)
