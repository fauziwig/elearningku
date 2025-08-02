from django.contrib import admin
from .models import CustomUser, UserProfile, UserActivity

# Mendaftarkan model CustomUser, UserProfile, dan UserActivity
admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(UserActivity)