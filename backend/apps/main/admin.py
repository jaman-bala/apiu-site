from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Photo
from .staff import Staff
from .additional import Video



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "created",
        "img1",
        "title1",
        "img2",
        "title2",
        "img3",
        "title3",
        "img4",
        "title4",
        "img5",
        "title5",
        "img6",
        "title6",
        "img7",
        "title7",
        "img8",
        "title8",
        "img9",
        "title9",
        "img10",
        "title10",            
    )
    search_fields = (
        "title",     
    )
    list_filter = (
        "is_active",
        "created",
    )

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img1.url}" style="max-height: 330px;">')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'is_active', 'created')
    search_fields = ('title',)
    list_filter = ("is_active", "created",)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'phone', 'email', 'kab', 'is_active', 'created',)
    search_fields = ('title', 'position', 'phone')
    list_filter = ("is_active", "created",)

