from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rental/all_rentals', views.all_rentals, name='rental'),
    path('rental/<int:pk>', views.rental_id, name='rental_id'),
    path('rental/add', views.rental_add, name='rental_add'),
    path('rental/customer/<int:pk>', views.customer_id, name='customer_id'),
    path('rental/customers', views.customers, name='customers'),
    path('rental/customer_add', views.customer_add, name='customers_add'),
    path('rental/vehicles', views.vehicles, name='vehicles'),
    path('rental/vehicle/<int:pk>', views.vehicle_id, name='vehicle_id'),
    path('rental/vehicle_add', views.vehicle_add, name='vehicle_add'),
]
"""

    /rent/vehicle/add – provide a form to add a new vehicle.
    See Below “Page Interaction”, to guide you with the templates
    """