from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('DONOR', 'Donor'),
        ('ACCEPTOR', 'Acceptor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='DONOR')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
