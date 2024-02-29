from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Actividad

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    Actividad.objects.create(usuario=user, accion='inicio de sesión')
