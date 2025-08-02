from django.contrib import admin
from .models import Material, Question, Choice

admin.site.register(Material)
admin.site.register(Question)
admin.site.register(Choice)