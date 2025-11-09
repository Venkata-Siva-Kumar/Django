from django.shortcuts import render,redirect,get_object_or_404
from .forms import BookingForm
from .models import PropertyBooking


# Create your views here.
PRICE_MAP = {
    'economy': 3000000,
    'luxury' : 5000000,
    'deluxe' : 7500000,
    'single' : 8000000,
    'duplex' : 10000000,
}

def home(request):
# data to show property types and prices
    flats = [
        ('economy', 'Economy flat', '30,00,000'),
        ('luxury', 'Luxury flat', '50,00,000'),
        ('deluxe', 'Deluxe flat', '75,00,000'),
    ]
    houses = [
        ('single', 'Single house', '80,00,000'),
        ('duplex', 'Duplex house', '1,00,00,000'),
    ]
    
    return render(request,'promoter/home.html',{'flats':flats,'houses':houses})


def register(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # determine amount
            if booking.booking_for == 'flat':
                booking.amount = PRICE_MAP.get(booking.flat_type, 0)
            else:
                booking.amount = PRICE_MAP.get(booking.house_type, 0)

            booking.save()
            return redirect('promoter:receipt', booking_id=booking.id)  # ✅ always returns something
        else:
            # even if invalid, return the form again
            return render(request, 'promoter/registration.html', {'form': form})
    else:
        form = BookingForm()
        return render(request, 'promoter/registration.html', {'form': form})


def receipt(request, booking_id):
    booking = get_object_or_404(PropertyBooking, id=booking_id)
    return render(request, 'promoter/receipt.html', {'booking': booking})

def view_booking(request):
    bookings = PropertyBooking.objects.all().order_by('-created_at')
    return render(request, 'promoter/view_booking.html', {'bookings': bookings})
