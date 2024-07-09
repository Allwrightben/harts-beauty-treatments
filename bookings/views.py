from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import Booking, TREATMENTS, TIME_SLOTS
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def bookings(request):
    return render(request, 'bookings.html', {'treatments': TREATMENTS, 'time_slots': TIME_SLOTS})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        # Check if all required fields are present
        required_fields = ['treatment', 'time_slot', 'date', 'message', 'name', 'phone']
        missing_fields = [field for field in required_fields if field not in request.POST]
        if missing_fields:
            # Construct an error message indicating which fields are missing
            error_message = "Please fill out all required fields."
            for field in missing_fields:
                error_message += f" {field.capitalize()} is required."
            
            # Redirect back to the booking page with the error message
            return HttpResponseRedirect(reverse('bookings') + '?error=' + error_message)
        
        # Validate form data
        try:
            treatment = int(request.POST['treatment'])
            time_slot = int(request.POST['time_slot'])
            date = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
            phone = int(request.POST['phone'])
        except ValueError:
            # Handle invalid input
            return HttpResponseRedirect(reverse('bookings') + '?error=Invalid%20input%20provided.')
        
        # Create a new booking
        Booking.objects.create(
            user=request.user,
            name=request.POST['name'],
            email=request.user.email,
            phone=request.POST['phone'],
            treatment=treatment,
            date=date,
            time=time_slot,
            message=request.POST['message'],
        )
        
        # Redirect to confirmation page
        return redirect('booking_confirmation')
    else:
        return redirect('bookings')

def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')

