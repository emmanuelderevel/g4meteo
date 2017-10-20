from django import forms

class NameForm(forms.Form):
    city_name = forms.CharField(label='Search for location', max_length=100)
