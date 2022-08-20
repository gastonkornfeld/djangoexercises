from django.contrib import admin
from .models import Rental, RentalRate, VehicleSize, VehicleType, Vehicle, Customer
# Register your models here.

admin.site.register(Rental)
admin.site.register(RentalRate)
admin.site.register(VehicleSize)
admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(Customer)
