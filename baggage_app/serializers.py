from rest_framework import serializers
from .models import Baggage

class BaggageSerializer(serializers.ModelSerializer):
    # This is for DISPLAY (reading)
    flight_number = serializers.ReadOnlyField(source='flight.flight_number')

    class Meta:
        model = Baggage
        # Added 'flight' to the list below so you can POST the ID
        fields = [
            'tag_id', 
            'passenger_name', 
            'weight_kg', 
            'is_overweight', 
            'status', 
            'flight',      
            'flight_number'
        ]