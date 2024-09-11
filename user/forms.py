from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class Reg(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class Change_usr(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email' ]


