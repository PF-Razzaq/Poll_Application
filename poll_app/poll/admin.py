from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('nationality',)
# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)