from django.contrib import admin
from .models import Car

@admin.register(Car)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['KPP_CHOICES', 'manufacturer', 'model', 'year', 'kpp', 'color']
