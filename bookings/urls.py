from django.urls import path
from .views import bookings, book_appointment, booking_confirmation

urlpatterns = [
    path('bookings/', bookings, name='bookings'),
    path('book/appointment/', book_appointment, name='book_appointment'),
    path('book/confirmation/', booking_confirmation, name='booking_confirmation'),
]