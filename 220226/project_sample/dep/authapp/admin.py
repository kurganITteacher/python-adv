# from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authapp.models import KpkUser


class KpkUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2'),
        }),
    )

    list_display = ('login', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('login', 'first_name', 'last_name', 'email')
    ordering = ('login',)


admin.site.register(KpkUser, KpkUserAdmin)
