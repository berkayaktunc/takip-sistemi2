from django.apps import AppConfig

class DbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Varsayılan birincil anahtar türü
    name = 'db'  # Uygulamanın adı
