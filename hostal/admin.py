from django.contrib import admin
from .models import Hostal,Reservacion
from django.utils.html import format_html

# Register your models here.

class HostalAdmin(admin.ModelAdmin):
    pass

class ReservacionAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('Reservado_Por',)
        return self.readonly_fields
    fieldsets = (
        ('Registrado a', {'fields': ('Nombre', 'Pasaporte','Email')}),
        ('Vuelo', {'fields': ('HoraEntrada','HoraSalida','Aerolinea')}),
        ('Detalles', {'fields': ('Personas','Reservado_Por')}),
    )
    list_display = ('Nombre','HoraEntrada','HoraSalida','Aerolinea','Reservado_Por','Detalles')
    def Detalles(self, obj):
        link = '/media/hostal/static/pdfs/%s' % obj.pdf  # 'admin:tesoreria_aportesobreros_change')
        return format_html('<a href="%s">%s</a>'%(link,"Descargar(PDF)") )
    list_filter = ['Reservado_Por','Aerolinea','Personas']
    search_fields = ['Nombre','Email','Pasaporte']

#admin.site.register(Hostal,HostalAdmin)
admin.site.register(Reservacion,ReservacionAdmin)