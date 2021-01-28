from hostal.views import HostalIndexView
from hostal.views import ReservacionesView


from django.urls import path


urlpatterns = [
    path('reservar/',HostalIndexView, name = 'hostal_reservar'),
    path('reservaciones/',ReservacionesView, name = 'reservaciones_detalles'),


  ]
 