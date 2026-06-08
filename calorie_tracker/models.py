from django.db import models
from datetime import date

class FoodItem(models.Model):
    """Simple model to store food items"""
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    date_added = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.calories} cal"