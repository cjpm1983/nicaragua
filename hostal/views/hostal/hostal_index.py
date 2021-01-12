from django.views.generic import ListView

from hostal.models import Hostal

class HostalIndexView(ListView):
    model = Hostal
    template_name = "hostal/index.html"
