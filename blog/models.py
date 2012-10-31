from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    publicacao = models.DateTimeField()
