from django.contrib import admin
from .models import Tender
from .vacancy import Vacancy
from .other import Other


admin.site.register(Tender)
admin.site.register(Vacancy)
admin.site.register(Other)
