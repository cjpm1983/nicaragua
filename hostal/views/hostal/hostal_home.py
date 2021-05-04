from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hostal.models import Reservacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def HomeView(request):
      
    return render(request,'hostal/home.html')
   