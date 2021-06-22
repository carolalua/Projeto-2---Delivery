from django.db import models
from django.contrib.auth import get_user_model
class Ingredientes(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    quantidade = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
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
        return f"{self.nome}, {self.preco}, {self.quantidade}, {self.status}"
class Receita(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    disponivel = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=now)
    data_ultima_atualizacao = models.DateTimeField(default=now)
    imagem = models.ImageField(upload_to='imagens-produtos', default='default.jpg')
    ingredientes = models.ManyToManyField(Ingredientes)
    def __str__(self):
        return self.nome
