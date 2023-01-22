from django.db import models

# Create your models here.

class Booking(models.Model):
    id=models.IntegerField(),
    name=models.CharField(),
    No_of_guests=models.IntegerField(),
    BookingDate=models.DateTimeField(),

class Menu(models.Model):
    id=models.IntegerField(),
    title=models.CharField(),
    price=models.DecimalField(),
    inventory=models.ImageField(),