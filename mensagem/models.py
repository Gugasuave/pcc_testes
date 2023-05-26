from django.db import models

# Create your models here.
class Usuarios(models.Model):
    idMensagem = models.IntegerField(primary_key = True)
    texto = models.CharField(max_length=1000)
    envia = models.CharField(max_length=45)
    topico = models.CharField(max_length=50)
    salaChat_idSala = models.ForeignKey("salaChat.Model", on_delete=models.CASCADE)
    salaChat_Usuarios_idUsuario = models.ForeignKey("salaChat.Model", on_delete=models.CASCADE)