from django.shortcuts import render
from django.views import generic
from .models import Treatment

# Create your views here.
class TreatmentList(generic.ListView):
    queryset = Treatment.objects.all()
    template_name = "treatment_list.html"


