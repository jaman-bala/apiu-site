from django.contrib import admin
from .models import File
from .disain import Disain
from .report import Report
from .study import Study
# Register your models here.



@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'file',
    )
    search_fields = ('title',)
    list_filter = ('created',)

@admin.register(Disain)
class DisainAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'file',
    )
    search_fields = ('title',)
    list_filter = ('created',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'file',
    )
    search_fields = ('title',)
    list_filter = ('created',)

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'file',
    )
    search_fields = ('title',)
    list_filter = ('created',)
