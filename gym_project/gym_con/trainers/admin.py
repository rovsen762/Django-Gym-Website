from django.contrib import admin
from . models import Trainer

@admin.register(Trainer) 
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)