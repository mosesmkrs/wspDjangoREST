from django.db import models
from django.core.validators import MinValueValidator

class RoomType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    reference_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    hotel_name = models.CharField(max_length=100, default="Blue Lagoon Hotels and Resorts")
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_rooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT)
    extra_bed = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    reservation_time = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.reference_number:
            # Generate a reference number if not provided
            self.reference_number = f"BL{self.id or 1000}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.customer_name}"