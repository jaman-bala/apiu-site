from django.contrib import admin
from .models import Photo
from .staff import Staff
from .additional import Video
# Register your models here.



admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Staff)
