from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.db import models 
from django.db.models import Sum, Count 
from django.shortcuts import render # Added for the Passenger Portal

from .models import Baggage
from flights.models import Flight 
from .serializers import BaggageSerializer

# ==========================================================
# 1. THE PASSENGER PORTAL (HTML VIEW)
# This is what passengers see when they visit the home page
# ==========================================================
def search_baggage(request):
    """
    The Home Page view for passengers.
    It looks for a 'tag_id' in the URL and returns the bag details to the HTML template.
    """
    query = request.GET.get('tag_id')
    baggage = None
    
    if query:
        # Case-insensitive search for the bag (e.g., fj123 vs FJ123)
        baggage = Baggage.objects.filter(tag_id__iexact=query).first()
        
    return render(request, 'baggage_app/search.html', {
        'baggage': baggage,
        'query': query
    })

# ==========================================================
# 2. STAFF GATEWAY (API VIEWS FOR .NET DASHBOARD)
# ==========================================================

# List, Search, Filter, and ORDERING
class StaffBaggageList(generics.ListCreateAPIView):
    queryset = Baggage.objects.all()
    serializer_class = BaggageSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Fields that can be searched (text search)
    search_fields = ['passenger_name', 'tag_id']
    
    # Fields that can be filtered (exact match)
    filterset_fields = ['status', 'flight', 'flight__flight_number']
    
    # Ordering configuration
    ordering_fields = ['weight_kg', 'timestamp']
    ordering = ['-timestamp'] # Show newest bags first


# Update status (LOADED/PENDING) via PATCH/PUT
class StaffBaggageUpdate(generics.UpdateAPIView):
    queryset = Baggage.objects.all()
    serializer_class = BaggageSerializer
    lookup_field = 'tag_id'


# ==========================================================
# 3. DATA GATEWAYS (FOR ANALYTICS & SPECIFIC LOOKUPS)
# ==========================================================

# Look up individual bag status (JSON API version)
class PassengerBagDetail(generics.RetrieveAPIView):
    queryset = Baggage.objects.all()
    serializer_class = BaggageSerializer
    lookup_field = 'tag_id'


# Summary logic for Flight Supervisors
class FlightBaggageSummary(APIView):
    def get(self, request, flight_id):
        # Filter bags for the specific flight
        bags = Baggage.objects.filter(flight_id=flight_id)
        
        # Calculate totals using Database Aggregation
        stats = bags.aggregate(
            total_bags=Count('id'),
            total_weight=Sum('weight_kg'),
            overweight_count=Count('id', filter=models.Q(is_overweight=True))
        )
        
        # Get flight number for the title
        try:
            flight = Flight.objects.get(id=flight_id)
            flight_num = flight.flight_number
        except Flight.DoesNotExist:
            flight_num = "Unknown"

        return Response({
            "flight_number": flight_num,
            "summary": {
                "total_bags": stats['total_bags'] or 0,
                "total_weight_kg": stats['total_weight'] or 0,
                "overweight_alerts": stats['overweight_count'] or 0,
            }
        })