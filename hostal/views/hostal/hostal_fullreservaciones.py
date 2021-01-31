""" from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hostal.models import Reservacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger """

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from hostal.models import Reservacion, Cliente
from hostal.forms import ChildFormset

class ReservacionListView(ListView):
    model = Reservacion
    template_name = 'hostal/reservacion_list.html'


class ParentCreateView(CreateView):
    model = Reservacion
    fields = ['Nombre','Pasaporte','Email','Imagen_Pasaporte','Imagen_Pasaje','HoraEntrada','HoraSalida','Observaciones','Aerolinea']
    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["clientes"] = ChildFormset(self.request.POST)
        else:
            data["clientes"] = ChildFormset()
        return data
    def form_valid(self, form):
        context = self.get_context_data()
        clientes = context["clientes"]
        self.object = form.save()
        if clientes.is_valid():
            clientes.instance = self.object
            clientes.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("parents:list")

class ParentUpdateView(UpdateView):
    model = Reservacion
    fields = ['Nombre','Pasaporte','Email','Imagen_Pasaporte','Imagen_Pasaje','HoraEntrada','HoraSalida','Observaciones','Aerolinea']
    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered.
        # the difference with CreateView is that
        # on this view we pass instance argument
        # to the formset because we already have
        # the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["clientes"] = ChildFormset(self.request.POST, instance=self.object)
        else:
            data["clientes"] = ChildFormset(instance=self.object)
        return data
    def form_valid(self, form):
        context = self.get_context_data()
        clientes = context["clientes"]
        self.object = form.save()
        if clientes.is_valid():
            clientes.instance = self.object
            clientes.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("parents:list")

    #return render(request,'hostal/reservaciones.html',{'reservaciones':reservaciones})
   