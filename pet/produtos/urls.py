from django.urls import path
from pet.produtos.views import produtos, servicos

urlpatterns = [
    path("produtos/", produtos, name="produtos"),
    path("servicos/", servicos, name="servicos"),
]
