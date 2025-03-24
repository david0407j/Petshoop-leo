from django.urls import path

from pet.base.views import base


app_name = "base"
urlpatterns = [
    path("", base, name="base"),
]