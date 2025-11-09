from django.contrib import admin
from .models import PropertyBooking

@admin.register(PropertyBooking)
class PropertyBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'booking_for', 'flat_type', 'house_type', 'amount', 'created_at')
    list_filter = ('booking_for', 'flat_type', 'house_type')
    search_fields = ('name', 'mobile', 'email')