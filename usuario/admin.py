from django.contrib import admin

# Register your models here.

from .models import UserProfile


from django.contrib.auth.admin import UserAdmin
from .forms import UserProfileCreationForm, UserProfileChangeForm
from django.utils.html import format_html


'''
class UsuariosAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile,UsuariosAdmin)
'''

class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ('username', 'is_staff', 'is_active')
    list_filter = ('username', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal_Data', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('groups', 'is_staff', 'is_active', 'is_superuser')}),
        #('Images', {'fields': ('avatar', 'background')}),
        # ('Dates', {'fields': ('last_login', 'date_joined')}),

        # ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    # add_fieldsets = (
    #     (None,{
    #         'classes':('wide',),
    #         'fields':('username','password1','password2','is_staff','is_active')
    #     })
    # )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(UserProfile,UserProfileAdmin)

