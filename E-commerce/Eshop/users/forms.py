from django import forms 

class Register(forms.Form):
    firstname = forms.CharField(max_length=70)
    lastname = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)