from django import forms
from .models import Plant_Details


class PlantDetailsForm(forms.ModelForm):
    class Meta:
        model = Plant_Details
        fields = '__all__'
        widgets = {
        'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Plant Name : '}),
        'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter type (Indoor/Outdoor)'}),
        'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
        'benefit': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter benefits'}),

        }