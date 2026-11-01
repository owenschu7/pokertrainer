from django import forms
from django.core import validators
from django.contrib.auth.models import User


# from midterm/suduku
# JoinForm is inherited from ModelForm
class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    class Meta():
        # tell the form which model it belongs to
        # in save() after you is_valid(request.POST) it will
        # - create a new User model
        # - fill it in with the data from the fields
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
        }

# from midterm/suduku
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
