"""
URL configuration for airport_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    # 1. THE API GATEWAYS (Technical data for the .NET Staff Dashboard)
    # These stay as they are so your C# app doesn't break
    path('api/baggage/', include('baggage_app.urls')),
    path('api/flights/', include('flights.urls')),

    
    # 2. THE PASSENGER PORTAL (The Home Page)
    # This makes http://127.0.0.1:8001/ show the tracking search bar
    path('', include('baggage_app.urls')), 
]