from django.db import models

class Baggage(models.Model):
    # This string reference tells Django: "Go look in the flights app for the Flight model"
    flight = models.ForeignKey('flights.Flight', on_delete=models.CASCADE, related_name="bags")
    
    passenger_name = models.CharField(max_length=100)
    tag_id = models.CharField(max_length=20, unique=True, help_text="Example: FJ12345")
    
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    is_overweight = models.BooleanField(default=False)
    
    STATUS_CHOICES = [
        ('CHECKED_IN', 'Checked-In at Counter'),
        ('SECURITY', 'Security Cleared'),
        ('LOADED', 'Loaded on Aircraft'),
        ('OFFLOADED', 'Offloaded / Security Alert'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CHECKED_IN')
    timestamp = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically flags weight over 30kg
        self.is_overweight = self.weight_kg > 30
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tag_id} ({self.status})"