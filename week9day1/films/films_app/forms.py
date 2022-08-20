
from django import forms

from .models import Film, Director


class AddFilmForm(forms.ModelForm):
    # name = forms.CharField()
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
            'release_date': forms.SelectDateWidget,
            'created_in': forms.RadioSelect,
            'available_in': forms.CheckboxSelectMultiple,
            'categories': forms.CheckboxSelectMultiple,
            'directors': forms.CheckboxSelectMultiple,
        }


class AddDirectorForm(forms.ModelForm):
    # name = forms.CharField()
    class Meta:
        model = Director
        fields = '__all__'



