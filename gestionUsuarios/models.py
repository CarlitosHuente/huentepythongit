from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

class Usuario(AbstractUser):
    email_validator = RegexValidator(
        regex='^[a-zA-Z0-9_.+-]+@huentelauquen\.cl$',
        message='El correo debe pertenecer al dominio @huentelauquen.cl'
    )
    email = models.EmailField(unique=True, validators=[email_validator])


class Actividad(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usuario} realizó {self.accion} en {self.fecha_hora}"
