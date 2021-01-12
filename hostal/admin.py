from django.contrib import admin
from .models import Hostal

# Register your models here.

class HostalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hostal,HostalAdmin)