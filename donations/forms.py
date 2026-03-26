from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['food_name', 'quantity', 'available_time', 'location', 'contact_details']
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. 50 boxes of pizza'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. 50 kg / 50 boxes'}),
            'available_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. 2 PM to 5 PM'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address, City'}),
            'contact_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone or Email'}),
        }
