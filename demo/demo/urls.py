"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
import demo.views as views

urlpatterns = [
    url(r"^user/logout$", views.UserLogout.as_view()),
    url(r"^user/login$", views.UserLogin.as_view()),
    url(r"^user/createWithList$", views.UserCreateWithList.as_view()),
    url(r"^user/createWithArray$", views.UserCreateWithArray.as_view()),
    url(r"^user/(?P<username>.+)$", views.UserUsername.as_view()),
    url(r"^user$", views.User.as_view()),
    url(r"^store/order/(?P<orderId>.+)$", views.StoreOrderOrderId.as_view()),
    url(r"^store/order$", views.StoreOrder.as_view()),
    url(r"^store/inventory$", views.StoreInventory.as_view()),
    url(r"^pet/findByTags$", views.PetFindByTags.as_view()),
    url(r"^pet/findByStatus$", views.PetFindByStatus.as_view()),
    url(r"^pet/(?P<petId>.+)/uploadImage$", views.PetPetIdUploadImage.as_view()),
    url(r"^pet/(?P<petId>.+)$", views.PetPetId.as_view()),
    url(r"^pet$", views.Pet.as_view()),
]

if settings.DEBUG:
    urlpatterns.extend([
        url(r"^the_specification/$", views.__SWAGGER_SPEC__.as_view()),
        url(r"^ui/(?P<path>.*)$", serve, {"document_root": "ui",
                                          "show_indexes": True})
    ])