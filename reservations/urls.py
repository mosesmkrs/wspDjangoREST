from django.urls import path
from .views import ReservationCreateView, ReservationDetailView

urlpatterns = [
    path('reservations/', ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/<str:reference_number>/', ReservationDetailView.as_view(), name='reservation-detail'),
]