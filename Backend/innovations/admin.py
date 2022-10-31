from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import OurUser

class OurUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'fio', 'bornAge', 'country', 'city', 'citizenship', 'sex', 'phone',
        'education', 'busyness', 'experience', 'skills', 'jopa',
        'isTeam', 'role', 'isAuthor', 'requisites', 'isCompany', 'inn',
        'image', 'description', 'project_likes', 'isForm', 'isActivated'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('fio', 'bornAge', 'country', 'city', 'citizenship', 'sex', 'phone',
        'education', 'busyness', 'experience', 'skills', 'jopa',
        'isTeam', 'role', 'isAuthor', 'requisites', 'isCompany', 'inn',
        'image', 'description', 'project_likes', 'isForm', 'isActivated')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('fio', 'bornAge', 'country', 'city', 'citizenship', 'sex', 'phone',
        'education', 'busyness', 'experience', 'skills', 'jopa',
        'isTeam', 'role', 'isAuthor', 'requisites', 'isCompany', 'inn',
        'image', 'description', 'project_likes', 'isForm', 'isActivated')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('fio', 'bornAge', 'country', 'city', 'citizenship', 'sex', 'phone',
        'education', 'busyness', 'experience', 'skills', 'jopa',
        'isTeam', 'role', 'isAuthor', 'requisites', 'isCompany', 'inn',
        'image', 'description', 'project_likes', 'isForm', 'isActivated')
        })
    )


admin.site.register(OurUser, OurUserAdmin)