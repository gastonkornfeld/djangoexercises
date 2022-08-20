from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Customer (models.Model):
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.firs_name} {self.last_name} {self.email}'


class VehicleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
    
class VehicleSize(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'



class Vehicle(models.Model):
    date_created = models.DateField(timezone.now())
    real_cost = models.IntegerField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name='types')
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE, related_name='sizes')
    
    def __str__(self):
        return f'{self.vehicle_type} {self.vehicle_size}'


class Rental(models.Model):
    rental_date = models.DateField(timezone.now())
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='rentals')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle')

    def __str__(self):
        return f'{self.rental_date} to {self.return_date}'

  
class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name='rentals')
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE, related_name='vehicle')



