from django.urls import path
from . import views
"""todas as urls referente a gestãoacademica deverão estar nesse aquivo"""
urlpatterns = [
 path('', views.listaIngredientes, name='lista-ingredientes'),
 path('cadastrarIngredientes/<int:id>', views.cadastrarIngredientes, name="cadastroI"),
]
