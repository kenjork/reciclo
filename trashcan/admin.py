from django.contrib import admin

# Register your models here.
from .models import TrashCan, Level

@admin.register(TrashCan)
class TrashCanAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'depth',
        'barcode',
        'address',
        'lng',
        'lat',
    )
    list_filter = (
        'depth',
    )
    search_fields = (
        'address',
        'barcode',
    )

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'trash_can',
        'time',
        'distance',
    )