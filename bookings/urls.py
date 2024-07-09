from django.urls import path
from .views import bookings, book_appointment, booking_confirmation, my_bookings, edit_booking, delete_booking

urlpatterns = [
    path('bookings/', bookings, name='bookings'),
    path('book/appointment/', book_appointment, name='book_appointment'),
    path('book/confirmation/', booking_confirmation, name='booking_confirmation'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('edit-booking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('delete-booking/<int:booking_id>/', delete_booking, name='delete_booking'),
]