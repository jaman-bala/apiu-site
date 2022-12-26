from django.contrib import admin
from .models import File
from .disain import Disain
from .report import Report
from .study import Study
# Register your models here.


admin.site.register(File)
admin.site.register(Report)
admin.site.register(Disain)
admin.site.register(Study)

