from django.urls import path
from .views import FlightList, FlightDetail

urlpatterns = [
    # Gateway for all flights
    path('', FlightList.as_view(), name='flight-list'),
    
    # Gateway for a specific flight by its number
    path('<str:flight_number>/', FlightDetail.as_view(), name='flight-detail'),
]