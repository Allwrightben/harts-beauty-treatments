from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from .views import handler404, handler500

urlpatterns = [
    path('bookings/', include("bookings.urls"), name="bookings-urls"),
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("treatments.urls"), name="treatments-urls"),  
]

handler404 = 'my_project.views.handler404'
handler500 = 'my_project.views.handler500'
