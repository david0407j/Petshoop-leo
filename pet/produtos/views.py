from django.shortcuts import render
from pet.produtos.models import Produto, Servico


def produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/produtos.html", {"produtos": produtos})


def servicos(request):
    servicos = Servico.objects.all()
    return render(request, "produtos/servicos.html", {"servicos": servicos})
