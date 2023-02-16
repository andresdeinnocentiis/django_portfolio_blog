from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, AnonymousUser

# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


class AnonymousUserAdmin(admin.ModelAdmin):
    model = AnonymousUser
    list_display = ['id', 'username', 'anonymous_identifier']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(AnonymousUser, AnonymousUserAdmin)