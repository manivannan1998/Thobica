from django import forms
from mainapp.models import User

class UserSuscribeForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'