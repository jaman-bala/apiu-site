from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Tender
from .vacancy import Vacancy
from .other import Other


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'title_contracts',
        'pricath',
        'text',
        'file',
        'date',
        'is_active',
        'created',
        'updated',
    )
    search_fields = ('title', 'title_contracts', 'pricath',)
    list_filter = ('created', 'is_active', 'updated',)


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'title',
        'text',
        'is_active',
        'created',
    )
    search_fields = ('country', 'title', 'text',)
    list_filter = ('is_active', 'created',)


@admin.register(Vacancy)
class Vacancy(admin.ModelAdmin):
    list_display = (
        'country',
        'title',
        'text',
        'file',
        'is_active',
        'date',
        'created',
        'updated',
    )
    search_fields = ('country', 'title', 'text',)
    list_filter = ('is_active', 'created', 'updated',)