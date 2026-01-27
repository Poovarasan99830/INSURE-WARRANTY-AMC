from django import forms
from .models import Appliances

class Appliance_form(forms.ModelForm):
    class Meta:
        model=Appliances
        fields='__all__'