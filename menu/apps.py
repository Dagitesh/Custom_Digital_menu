from django.apps import AppConfig
import cloudinary.api
from cloudinary.exceptions import Error

class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
    def ready(self):
        try:
            cloudinary.api.ping()
            print("✅ Cloudinary connection successful!")
        except Error as e:
            print("❌ Cloudinary connection failed:", e)