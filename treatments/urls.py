from . import views
from django.urls import path

urlpatterns = [
    path('', views.TreatmentList.as_view(), name='home'),
    path('<slug:slug>/', views.treatment_detail, name='treatment_detail'),
]
