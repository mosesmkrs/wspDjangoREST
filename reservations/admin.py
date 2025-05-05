from django.contrib import admin
from .models import Reservation, RoomType

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reference_number', 'customer_name', 'check_in_date', 'check_out_date', 'total_amount')
    readonly_fields = ('reference_number', 'total_amount', 'reservation_time')

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_night', 'capacity')