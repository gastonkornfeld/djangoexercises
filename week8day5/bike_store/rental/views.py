from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Customer,Rental, Vehicle
from .forms import AddRentalForm, AddCustomerForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_rentals(request):
    """
    show a list of all rentals, unreturned first, then ordered by date ascending (earliest first)
    """
    all_rentals = Rental.objects.all().order_by('return_date')
    return render(request, 'all_rental.html', {"all_rentals": all_rentals})

def rental_id(request, pk):

    rental = Rental.objects.get(id=pk)
    """
    show the information about the given rental
    """
    return render(request, 'rental_id.html', {'id':pk, 'rental':rental})



def rental_add(request):
    """
    provide a form to enter a customer ID and a vehicle ID to create a rental.
    If the customer or the vehicle does not exist, show a user-friendly error message.
    If the vehicle is currently being rented, show a relevant error message.
    """
    if request.method == 'POST':
        form = AddRentalForm(request.POST)
        if form.is_valid():
            cust_id = form.cleaned_data['costumer_id']
            customer = Customer.objects.get(id=cust_id)
            vehicle_id = form.cleaned_data['vehicle_id']
            vehicle = Vehicle.objects.get(id=vehicle_id)

            rental_date = form.cleaned_data['rental_date']
            return_date = form.cleaned_data['return_date']

            newRental = Rental(rental_date=rental_date, return_date=return_date, customer = customer, vehicle = vehicle)
            newRental.save()
            print('saved')
            context = {'form': form}
            return redirect('rental')
        return HTTPResponse('Your form is not valid reload the page')


    form = AddRentalForm()
    context = {'form': form}
    return render(request, 'rental_add.html', context)


def customer_id(request, pk):
    """
    show the customer matching the given ID
    """

    customer = Customer.objects.get(id=pk)
    return render(request, 'customer_id.html', {'id':pk, "customer": customer})

def customers(request):
    """
    Show all customers and his rentalsa
    """
    all_customers = Customer.objects.all().order_by('firs_name')

    return render(request, 'customers.html', {"customers": all_customers})

def customer_add(request):
    """
    provide a form to add a new customer
    """
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            new_customer = Customer(firs_name = first_name, last_name = last_name, phone_number= phone_number, email = email, address = address, country = country, city = city)
            new_customer.save()
            print('customer saved')

            
            return redirect('customers')
        return HTTPResponse('Your form is not valid reload the page')


    form = AddCustomerForm()
    context = {'form': form}
    return render(request, 'customer_add.html', context)



def vehicles(request):
    """
    Show all vehicles in the store
    """
    return render(request, 'vehicles.html')


def vehicle_add(request):
    """
    provide a form to add a new vehicle
    """
    return render(request, 'vehicle_add.html')



def vehicle_id(request, pk):
    """
    Show one of the vehicles by his id and if it is rented
    """
    return render(request, 'vehicle_id.html', {'id':pk})



