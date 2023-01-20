from django.contrib import admin
from django.forms.widgets import ClearableFileInput
from .models import Library

class LibraryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        Library._meta.get_field('image'): {'widget': ClearableFileInput},
    }

admin.site.register(Library, LibraryAdmin)




