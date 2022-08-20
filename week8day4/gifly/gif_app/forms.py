from django import forms

class CategoryForm(forms.Form):

    name = forms.CharField(min_length=3, max_length=50)