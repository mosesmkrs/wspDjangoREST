import uuid
from django.db import models

class RoomType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    reference_number = models.CharField(max_length=20, unique=True, editable=False)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    hotel_name = models.CharField(max_length=100, default="Blue Lagoon Hotels and Resorts")
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_rooms = models.PositiveIntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT)
    extra_bed = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    reservation_time = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = self.generate_reference_number()
        if not self.total_amount:
            self.calculate_total()
        super().save(*args, **kwargs)

    def generate_reference_number(self):
        return f"BL{uuid.uuid4().hex[:8].upper()}"

    def calculate_total(self):
        nights = (self.check_out_date - self.check_in_date).days
        base_price = self.room_type.price_per_night * nights * self.number_of_rooms
        extra_bed_price = 10000 if self.extra_bed else 0
        self.total_amount = base_price + extra_bed_price

    def __str__(self):
        return f"{self.reference_number} - {self.customer_name}"