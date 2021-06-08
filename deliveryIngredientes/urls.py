from django.urls import path
from . import views
"""todas as urls referente a gestãoacademica deverão estar nesse aquivo"""
urlpatterns = [
 path('', views.listar_receitas, name='lista-receitas'),
 path('detalhes_produto/<int:id>', views.detalhes_produto, name="detalhes"),
]
