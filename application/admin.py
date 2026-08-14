from django.contrib import admin
from .models import Service, Equipe, Equipement, Space


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order']
    list_editable = ['order']


@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']

