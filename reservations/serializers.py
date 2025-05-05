from rest_framework import serializers
from .models import Reservation, RoomType

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'name', 'description', 'price_per_night', 'capacity']

class ReservationSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(read_only=True)
    room_type_id = serializers.PrimaryKeyRelatedField(
        queryset=RoomType.objects.all(),
        source='room_type',
        write_only=True
    )
    hotel_name = serializers.CharField(default="Blue Lagoon Hotels and Resorts", read_only=True)
    total_amount = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    reference_number = serializers.CharField(read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'reference_number',
            'customer_name',
            'customer_email',
            'customer_phone',
            'hotel_name',
            'check_in_date',
            'check_out_date',
            'number_of_rooms',
            'room_type',
            'room_type_id',
            'extra_bed',
            'total_amount',
            'reservation_time',
            'is_confirmed'
        ]
        read_only_fields = ['reference_number', 'reservation_time', 'is_confirmed']

    def validate(self, data):
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError("Check-out date must be after check-in date")
        return data