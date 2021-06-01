from django.contrib import admin
# Register your models here.
from .models import Ingredientes, Receita
admin.site.register(Ingredientes)
admin.site.register(Receita)
