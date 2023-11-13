# this is more of a config or settings file
from django.apps import AppConfig


class FirstAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first_app'
