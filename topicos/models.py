from django.db import models

# Create your models here.
class Topicos(models.Model):
    idTopicos = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length=45)
    data = models.DateField()
    horario = models.TimeField()
    criador = models.CharField(max_length=45)