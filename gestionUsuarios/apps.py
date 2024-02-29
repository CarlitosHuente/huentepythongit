from django.apps import AppConfig

class GestionUsuariosConfig(AppConfig):
    name = 'gestionUsuarios'

    def ready(self):
        import gestionUsuarios.signals  # Asegúrate de usar la ruta correcta a tu archivo signals.py
