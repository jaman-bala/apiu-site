from django.contrib import admin
from .models import Photo
from .additional import Info
# Register your models here.
admin.site.register(Photo)
admin.site.register(Info)