from django.urls import path

from . import views

urlpatterns = [
    path('reservacion/',views.registro, name = 'registro'),
]