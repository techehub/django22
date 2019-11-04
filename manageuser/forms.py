
from django import forms

class UserReg (forms.Form):
    firstName = forms.CharField(max_length=50, label="First Name")
    lastName = forms.CharField(max_length=50, label="Last Name")
    emailName = forms.EmailField(max_length=50, label="Email Name")
    password = forms.CharField(max_length=50, label="Password")

