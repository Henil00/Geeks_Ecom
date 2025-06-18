from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

class StockMovement(models.Model):
    REASON_CHOICES = [
        ('sale', 'Sale'),
        ('restock', 'Restock'),
        ('adjustment', 'Adjustment'),
        ('return', 'Return'),
    ]

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='stock_movements')
    change = models.IntegerField(help_text='Positive for increase, negative for decrease')
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.product.name}: {self.change} ({self.reason}) on {self.timestamp.date()}"