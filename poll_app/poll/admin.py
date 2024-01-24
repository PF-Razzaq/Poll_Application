from django.contrib import admin
from .models import UserProfile,SaveRecord

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('nationality',)
# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SaveRecord)

