from datetime import datetime
from email.policy import default
from django import forms

class HelpTextContactForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text='100 characters max.')
    message = forms.CharField()
    sender = forms.EmailField(help_text='A valid email address, please.')
    cc_myself = forms.BooleanField(required=False, help_text= 'Done')

class AddBookForm(forms.Form):
    title = forms.CharField(max_length=100, help_text='title')
    date = forms.DateField(initial=datetime.now())
    reed_already = forms.BooleanField()