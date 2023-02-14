from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Create



@admin.register(Create)
class CreateAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'city',
        'phone',
        'title',
        'text',
        'file',
        'created',
    )
    list_filter = (
        'created',
    )
    search_fields = (
        'first_name',
        'last_name',
        'phone',
        'title',
        'file',
    )



