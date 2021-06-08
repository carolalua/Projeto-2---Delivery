from django.shortcuts import render, get_object_or_404, redirect
from .models import Receita

def listar_receitas(request):
    lista_receita = Receita.objects.filter(disponivel=True)
    contexto = {
        'Receita': Receita,
    }
    return render(request, 'deliverydeIngredientes/index.html', contexto)

def detalhes_produto(request):
    produto = get_object_or_404(Produto, id=id,disponivel=True)
    contexto = {
        'Receita': Receita,
    }
    return render (request, 'deliverydeIngredientes/detalhe.html', contexto)
