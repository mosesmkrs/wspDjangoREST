from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        response_data = {
            'reservationReference': serializer.data['reference_number'],
            'hotelName': serializer.data['hotel_name'],
            'totalAmount': serializer.data['total_amount'],
            'checkInDate': serializer.data['check_in_date'],
            'checkOutDate': serializer.data['check_out_date'],
            'confirmationTime': serializer.data['reservation_time'],
            'customerSupport': "+254700112233",
            'message': "Reservation successful. Please present this reference at check-in."
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'reference_number'
