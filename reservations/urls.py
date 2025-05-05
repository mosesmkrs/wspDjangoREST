from django.urls import path
from .views import (
    ReservationCreateView,
    ReservationListView,
    ReservationDetailView
)

urlpatterns = [
    path('reservations/', ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/list/', ReservationListView.as_view(), name='reservation-list'),
    path('reservations/<str:reference_number>/', ReservationDetailView.as_view(), name='reservation-detail'),
]