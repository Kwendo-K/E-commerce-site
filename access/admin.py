from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class AdminProfile(UserAdmin):
    inlines = [ProfileInline]


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, AdminProfile)
