from django.shortcuts import render, get_object_or_404, redirect
from .models import Receita

def listar_receitas(request):
    lista_receita = Receita.objects.all

    return render(request, 'deliveryIngredientes/index.html', {'receitas':lista_receita})

@login_required
def detalhes_produto(request, id):
    
    produto = get_object_or_404(Receita, id=id)

    return render (request, 'deliverydeIngredientes/detalhe.html', {'receita': produto})
