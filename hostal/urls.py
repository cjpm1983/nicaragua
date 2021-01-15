from hostal.views import HostalIndexView
from hostal.views import HostalDetallesView


from django.urls import path


urlpatterns = [
    path('',HostalIndexView, name = 'hostal_index'),
    path('detalles/<int:hostal_id>/',HostalDetallesView, name = 'hostal_detalles'),

  ]
 