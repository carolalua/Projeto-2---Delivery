from django.db import models
from django.contrib.auth import get_user_model
class Categoria(models.Model):
    STATUS = (
        ('proteina', 'Proteina'),
        ('frutas', 'Frutas'),
        ('legumes', 'Legumes'),
    )
    status = models.CharField(
        max_length=11,
        choices=STATUS,
    )
    def __str__(self):
        return f"{self.status}"
    
class Ingredientes(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    quantidade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    categoria = models.ForeignKey('Categoria', verbose_name="Categoria", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nome}, {self.preco}, {self.quantidade}, {self.categoria}"
class Receita(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    descricao = models.TextField()
    ingrediente = models.ForeignKey('Ingredientes', verbose_name="Ingredientes", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nome},{self.preco},{self.descricao}"
