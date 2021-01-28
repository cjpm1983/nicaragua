from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hostal.models import Reservacion

@login_required(login_url="")
def ReservacionesView(request):
    reservaciones = Reservacion.objects.filter(Reservado_Por=request.user)

    
    return render(request,'hostal/reservaciones.html',{'reservaciones':reservaciones})
   