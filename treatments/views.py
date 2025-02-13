from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Treatment


# view for listing treatments
class TreatmentList(generic.ListView):
    queryset = Treatment.objects.filter(status=1)
    template_name = "treatments/index.html"
    # paginate by 3 treatments per page
    paginate_by = 3


def treatment_detail(request, slug):

    queryset = Treatment.objects.filter(status=1)
    treatment = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "treatments/treatment_detail.html",
        {"treatment": treatment},
    )
