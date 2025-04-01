from django.contrib import admin
from .models import Produto, Servico


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")
    search_fields = ("nome",)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")
    search_fields = ("nome",)
