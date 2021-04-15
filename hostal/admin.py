from django.contrib import admin
from .models import Hostal,Reservacion,Aerolinea,Cliente
from django.utils.html import format_html

# Register your models here.

class HostalAdmin(admin.ModelAdmin):
    pass

class AerolineaAdmin(admin.ModelAdmin):
    pass

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Reservado_en','Pasaporte','Email','Imagen_Pasaporte','Imagen_Pasaje')
    #list_filter = ['Reservacion']
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('Reservacion',)
        return self.readonly_fields
    
    def Reservado_en(self, obj):
        link = '/admin/hostal/reservacion/%s/change/' % obj.Reservacion.id
        return format_html('<a href="{}">{}</a>', link, obj.Reservacion)
    

class ReservacionAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('aNombre','Reservado_Por')
        return self.readonly_fields
    fieldsets = (
        ('Registrado a', {'fields': ('aNombre',)}),
        ('Vuelo', {'fields': ('HoraEntrada','HoraSalida','Aerolinea')}),
        ('Detalles', {'fields': ('Personas','Reservado_Por','Observaciones')}),
    )

    list_display = ('aNombre','Clientes','HoraEntrada','HoraSalida','Aerolinea','Reservado_Por','Detalles')

    def Clientes(self, obj):
        link = '/admin/hostal/cliente/?Reservacion__id__exact=%d' % obj.id  # 'admin:tesoreria_aportesobreros_change')
        return format_html('<a href="{}">{}</a>', link,
                            '%d Clientes' % Cliente.objects.filter(Reservacion=obj.id).count())

    def Detalles(self, obj):
        link = '/media/hostal/static/pdfs/%s' % obj.pdf  # 'admin:tesoreria_aportesobreros_change')
        return format_html('<a href="%s">%s</a>'%(link,"Descargar(PDF)") )

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user.is_superuser:
                return True
            else: 
                if obj.user != request.user:
                    return False
                else:
                    return True

    list_filter = ['Reservado_Por','Aerolinea','Personas']
    search_fields = ['aNombre']

#admin.site.register(Hostal,HostalAdmin)
admin.site.register(Reservacion,ReservacionAdmin)
admin.site.register(Aerolinea,AerolineaAdmin)
admin.site.register(Cliente,ClienteAdmin)