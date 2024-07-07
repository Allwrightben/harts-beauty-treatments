from django.shortcuts import render, redirect
from .models import Booking, TREATMENTS, TIME_SLOTS
from django.contrib.auth.decorators import login_required

@login_required
def bookings(request):
    return render(request, 'bookings.html', {'treatments': TREATMENTS, 'time_slots': TIME_SLOTS})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        # Extract form data
        treatment = request.POST['treatment']
        time_slot = request.POST['time_slot']
        date = request.POST['date']
        message = request.POST['message']
        name = request.POST['name']
        
        # Create a new booking
        Booking.objects.create(
            user=request.user,
            name=name,
            email=request.user.email,
            phone=request.POST['phone'],
            treatment=treatment,
            date=date,
            time=time_slot,
            message=message,
        )
        
        # Redirect to a confirmation page or dashboard
        return redirect('booking_confirmation')
    else:
        return redirect('bookings')

def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')

