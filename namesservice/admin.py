from django.contrib import admin

from .models import SimpleName


@admin.register(SimpleName)
class SimpleNameAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_filter = ('created', )
