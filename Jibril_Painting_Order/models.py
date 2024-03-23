from django.db import models
from Jibril_Painting_Item.models import Painting


class Order(models.Model):
    player_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)  # Reminder: storing passwords should be done securely
    address = models.TextField()
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order by {self.full_name}"

class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.customer_id}"

