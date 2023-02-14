from django.contrib import admin
from django.utils.safestring import mark_safe
from django.forms.widgets import ClearableFileInput
from .models import Library


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image",
        "author",
        "is_active",
        "books",
    )
    search_fields = (
        "title",
        "author",
        

    )
    list_filter = (
        "is_active",
        "created",
    )

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 330px;">')





