from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        try:
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
        except IntegrityError:
            return Response(
                {"error": "Failed to generate unique reference number"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'reference_number'