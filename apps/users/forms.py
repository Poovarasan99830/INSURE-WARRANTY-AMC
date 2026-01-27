from django import forms
from .models import Register
from django.contrib.auth.models import User

class registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields=['bio']

class userfrom(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
    

