# spa/forms.py
from django import forms

class SpaSearchForm(forms.Form):
    keyword = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search for spas...'}),
    )                   