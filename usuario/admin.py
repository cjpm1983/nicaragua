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
    list_display = ('username','first_name', 'last_name','is_staff', 'is_active')
    list_filter = ('is_active',)

    fieldsets = (
        ("Autenticacion", {'fields': ('username', 'password')}),
        ('Informacion Personal', {'fields': ('first_name', 'last_name','email','Telefono')}),
        ('Permisos', {'fields': ('groups', 'is_staff', 'is_active', 'is_superuser')}),
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
    search_fields = ('username','first_name','last_name','email')
    ordering = ('username',)

admin.site.register(UserProfile,UserProfileAdmin)

