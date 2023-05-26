from django.db import models

# Create your models here.
class Usuarios(models.Model):
    idUsuario = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length=150)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=50)
    dataNasc = models.DateField()
    tipo = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    crp = models.IntegerField()