from django.contrib import admin
from .models import Booking

'''
This registers the Booking model with the 
Django admin site using the admin.ModelAdmin.
'''


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'email', 'phone', 'treatment', 'date',
        'time', 'message', 'created_at')
    list_filter = ('treatment', 'date', 'time', 'created_at')
    search_fields = (
        'user', 'email', 'phone', 'treatment',
        'date', 'time', 'message', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
