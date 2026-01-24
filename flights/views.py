from rest_framework import generics
from .models import Flight
from .serializers import FlightSerializer

# View for: /api/flights/
class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# View for: /api/flights/FJ911/
class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'flight_number' # Use the flight number to search instead of ID