from django import forms 
from .models import PropertyBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = PropertyBooking
        fields = ['name','mobile','email','booking_for','flat_type','house_type']
        
    def clean(self):
        cleaned = super().clean()
        booking_for = cleaned.get('booking_for')
        flat_type   = cleaned.get('flat_type')
        house_type  = cleaned.get('house_type')
        
        if booking_for == 'flat' and not flat_type:
            raise forms.ValidationError('Please select a flat type when booking for a flat.')
        
        if booking_for == 'house' and not house_type:
            raise forms.ValidationError('Please select a house type when booking for an independent house.')
        
        return cleaned