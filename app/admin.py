from django.contrib import admin
from .models import Testimonio

@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'estado', 'publicado', 'fecha_envio')
    list_filter = ('estado', 'publicado')
    search_fields = ('titulo', 'contenido', 'usuario__username')