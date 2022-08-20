


from django import forms

class AddRentalForm(forms.Form):
    costumer_id = forms.IntegerField()
    vehicle_id = forms.IntegerField()
    rental_date = forms.DateField(widget = forms.SelectDateWidget)
    return_date = forms.DateField(widget = forms.SelectDateWidget)


class AddCustomerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    email= forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)



