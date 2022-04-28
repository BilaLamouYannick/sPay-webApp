from django.apps import AppConfig


class OauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OAuth'

    def ready(self):
            import OAuth.signals