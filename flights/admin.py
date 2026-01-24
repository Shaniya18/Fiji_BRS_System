from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    # Columns to show in the list view
    list_display = ('flight_number', 'destination', 'departure_time', 'gate_number')
    
    # Add a search bar for flight numbers and destinations
    search_fields = ('flight_number', 'destination')
    
    # Add a filter sidebar on the right
    list_filter = ('departure_time', 'destination')
    
    # Make the list clickable by flight number
    list_display_links = ('flight_number',)