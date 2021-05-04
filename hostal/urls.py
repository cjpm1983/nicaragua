from hostal.views import HostalIndexView
from hostal.views import ReservacionesView
from hostal.views import HomeView
#from hostal.views import ParentCreateView


from django.urls import path


urlpatterns = [
    path('',HomeView, name = 'home'),
    path('reservar/',HostalIndexView, name = 'hostal_reservar'),
    path('reservaciones/',ReservacionesView, name = 'reservaciones_detalles'),
    #path('fullreservaciones/',ReservacionListView.as_view(), name = 'fullreservaciones_detalles'),
    #path('fullreservaciones/create/',ParentCreateView.as_view(), name = 'fullreservaciones_detalles'),
  ]
 