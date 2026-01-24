from django.urls import path
from . import views  # Import your function-based views (like search_baggage)
from .views import (
    StaffBaggageList, 
    PassengerBagDetail, 
    FlightBaggageSummary,
    StaffBaggageUpdate
)

# This allows you to use {% url 'baggage:search_baggage' %} in your templates
app_name = 'baggage'

urlpatterns = [
    # 1. THE MAIN PASSENGER PORTAL (The "Google" Home Page)
    # Accessible via: http://127.0.0.1:8001/
    path('', views.search_baggage, name='search_baggage'),

    # 2. STAFF GATEWAY (Used by your .NET C# Dashboard)
    # Accessible via: http://127.0.0.1:8001/staff/
    path('staff/', StaffBaggageList.as_view(), name='staff-list'),
    
    # 3. UPDATE GATEWAY (The "Confirm Load" Bridge for .NET)
    path('staff/<str:tag_id>/', StaffBaggageUpdate.as_view(), name='staff-update'),

    # 4. PASSENGER DATA API (Technical JSON data)
    path('track/<str:tag_id>/', PassengerBagDetail.as_view(), name='passenger-track'),

    # 5. SUMMARY GATEWAY (For supervisors)
    path('summary/<int:flight_id>/', FlightBaggageSummary.as_view(), name='flight-summary'),
]