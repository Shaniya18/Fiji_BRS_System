from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True) 
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    gate_number = models.CharField(max_length=5, default="G1")

    def __str__(self):
        return f"{self.flight_number} to {self.destination}"