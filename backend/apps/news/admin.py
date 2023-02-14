from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Articles



@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'full_text',
        'img',
        'date',
        'is_active',
        'created',
    )
    list_filter = (
        'is_active',
        'created',
    )
    search_fields = (
        'title',
        'full_text',
    )
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" style="max-height: 330px;">')






