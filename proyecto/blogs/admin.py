from django.contrib import admin
from .models import Blog

# Registra el modelo Blog para que sea administrable desde el panel de administración
admin.site.register(Blog)

