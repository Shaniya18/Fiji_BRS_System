from django.contrib import admin
from .models import Baggage

@admin.register(Baggage)
class BaggageAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'passenger_name', 'weight_kg', 'is_overweight', 'status', 'flight')
    list_filter = ('status', 'is_overweight', 'flight')
    search_fields = ('tag_id', 'passenger_name')
    
    # This makes the "is_overweight" column read-only in the admin 
    # so people don't manually change what the logic calculated
    readonly_fields = ('is_overweight',)