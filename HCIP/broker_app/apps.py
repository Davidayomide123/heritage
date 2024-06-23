from django.apps import AppConfig


class BrokerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'broker_app'

    def ready(self):
        from . import signals  # Import signals to connect them
