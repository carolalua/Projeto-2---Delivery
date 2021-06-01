from django.shortcuts import render, get_object_or_404, redirect
from .models import Ingredientes, Receita

def listaIngredientes(request):
    receita_i = Ingredientes.objects.all
    return render(request, 'deliveryIngredientes/index.html', {'receita':receita_i})
    
def cadastrarIngredientes(request, id):
    criarIngredientes = get_object_or_404(Receita, pk=id)
    criarIngredientes.save()
    return redirect('/')
