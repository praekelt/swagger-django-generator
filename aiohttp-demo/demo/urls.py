"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
import demo.views as views
import aiohttp_cors

def add_routes(app, with_ui=False):
    app.router.add_view(r"/user/{username}", views.UserUsername)
    app.router.add_view(r"/user/logout", views.UserLogout)
    app.router.add_view(r"/user/login", views.UserLogin)
    app.router.add_view(r"/user/createWithList", views.UserCreateWithList)
    app.router.add_view(r"/user/createWithArray", views.UserCreateWithArray)
    app.router.add_view(r"/user", views.User)
    app.router.add_view(r"/store/order/{orderId}", views.StoreOrderOrderId)
    app.router.add_view(r"/store/order", views.StoreOrder)
    app.router.add_view(r"/store/inventory", views.StoreInventory)
    app.router.add_view(r"/pet/{petId}/uploadImage", views.PetPetIdUploadImage)
    app.router.add_view(r"/pet/{petId}", views.PetPetId)
    app.router.add_view(r"/pet/findByTags", views.PetFindByTags)
    app.router.add_view(r"/pet/findByStatus", views.PetFindByStatus)
    app.router.add_view(r"/pet", views.Pet)
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