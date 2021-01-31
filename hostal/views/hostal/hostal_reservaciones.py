from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hostal.models import Reservacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url="")
def ReservacionesView(request):
    #reservaciones = Reservacion.objects.filter(Reservado_Por=request.user)

    reservaciones_list = Reservacion.objects.filter(Reservado_Por=request.user).order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(reservaciones_list, 5)
    try:
        reservaciones = paginator.page(page)
    except PageNotAnInteger:
        reservaciones = paginator.page(1)
    except EmptyPage:
        reservaciones = paginator.page(paginator.num_pages)

    
    return render(request,'hostal/reservaciones.html',{'reservaciones':reservaciones})
   