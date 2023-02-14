from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Gallery




@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo_add', 'country', 'date', 'created')
    search_fields = ('title',)
    list_filter = ('is_active', 'created')

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo_add.url}" style="max-height: 330px;">')
