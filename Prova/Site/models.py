from django.db import models

# Create your models here.

class Nota(models.Model):
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)