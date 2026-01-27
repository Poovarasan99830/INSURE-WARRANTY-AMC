from django import forms


from django.contrib.auth.models import User

from .models import Profile

class UserView(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username","email","password"]
    


class ProfileView(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["bio","avatars"]


