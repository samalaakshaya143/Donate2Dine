from django.db import models
from django.conf import settings

class FoodItem(models.Model):
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('CLAIMED', 'Claimed'),
        ('COLLECTED', 'Collected'),
    )

    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donated_items')
    food_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)
    available_time = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='AVAILABLE')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} by {self.donor.username}"

class FoodClaim(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='claims')
    acceptor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='claims')
    claimed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.acceptor.username} claimed {self.food_item.food_name}"
