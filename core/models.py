from django.db import models

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco_original = models.DecimalField(max_digits=10, decimal_places=2)
    preco_desconto = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_semanas = models.IntegerField()

    def __str__(self):
        return self.nome

# Create your models here.
