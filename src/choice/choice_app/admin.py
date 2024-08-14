from django.contrib import admin
from .models import Screen

@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ('screen_id', 'probability', 'fun_fact')
