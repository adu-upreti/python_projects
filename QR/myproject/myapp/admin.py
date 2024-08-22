from django.contrib import admin
from .models import *

@admin.register(GenerateImage)
class GenerateImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'imag')


@admin.register(DecodeImage)
class DecodeImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'imag')   
