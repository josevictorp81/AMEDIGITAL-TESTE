from django.contrib import admin

from .models import Planet

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ['name', 'climate', 'terrain', 'films_apparitions']
    list_filter = ['name', 'climate', 'terrain', 'films_apparitions']
