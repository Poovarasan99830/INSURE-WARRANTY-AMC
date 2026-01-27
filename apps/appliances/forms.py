from django import forms
from .models import Appliance


class APPLIANCE(forms.ModelForm):
    class Meta:
        model=Appliance
        fields="__all__"

        