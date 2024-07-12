from django.shortcuts import (
    render, redirect, HttpResponseRedirect, get_object_or_404
)
from django.urls import reverse
from .models import Booking, TREATMENTS, TIME_SLOTS
from django.contrib.auth.decorators import login_required
from django import forms
import datetime


@login_required
def bookings(request):
    return render(
        request, 'bookings.html',
        {'treatments': TREATMENTS, 'time_slots': TIME_SLOTS}
    )


@login_required
def book_appointment(request):
    if request.method == 'POST':
        # Check if all required fields are present
        required_fields = [
            'treatment', 'time_slot', 'date', 'message', 'name', 'phone'
        ]
        missing_fields = [
            field for field in required_fields if field not in request.POST
        ]
        if missing_fields:
            # Construct an error message indicating which fields are missing
            error_message = "Please fill out all required fields."
            for field in missing_fields:
                error_message += f" {field.capitalize()} is required."

            # Redirect back to the booking page with the error message
            return HttpResponseRedirect(
                reverse('bookings') + '?error=' + error_message
            )

        # Validate form data
        try:
            treatment = int(request.POST['treatment'])
            time_slot = int(request.POST['time_slot'])
            date = datetime.datetime.strptime(
                request.POST['date'], '%Y-%m-%d'
            ).date()
            phone = request.POST['phone']
        except ValueError:
            # Handle invalid input
            return HttpResponseRedirect(
                reverse('bookings') + '?error=Invalid%20input%20provided.'
            )

        # Create a new booking
        Booking.objects.create(
            user=request.user,
            name=request.POST['name'],
            email=request.user.email,
            phone=phone,
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


# View to display all bookings made by the current user
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})


# allows the user to edit a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'phone', 'treatment', 'date', 'time', 'message'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = self.instance.name
        self.fields['email'].initial = self.instance.email
        self.fields['phone'].initial = self.instance.phone
        self.fields['treatment'].initial = self.instance.treatment
        self.fields['date'].initial = self.instance.date
        self.fields['time'].initial = self.instance.time
        self.fields['message'].initial = self.instance.message


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html',
                  {'booking': booking, 'form': form})


# allows the user to delete a booking
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('my_bookings')
