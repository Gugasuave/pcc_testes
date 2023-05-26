from django.db import models

# Create your models here.
class Topicos(models.Model):
    idSala = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length=45)
    descricao = models.IntegerField(max_length=500)
    horarioCriacao = models.TimeField()
    dataCriacao = models.DateField()
    idUsuarios = models.ForeignKey("Usuarios.Model", on_delete=models.CASCADE)