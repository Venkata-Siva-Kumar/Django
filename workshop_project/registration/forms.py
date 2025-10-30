from django import forms
from .models import WorkshopRegistration
import re

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = WorkshopRegistration
        fields = ['name', 'dob', 'mobile', 'email', 'category']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match("^[A-Za-z ]+$", name):
            raise forms.ValidationError("Name should contain only letters and spaces.")
        return name

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match(r'^[6-9]\d{9}$', mobile):
            raise forms.ValidationError("Enter a valid 10-digit mobile number starting with 6-9.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Enter a valid email address.")
        return email
