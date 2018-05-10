from django import forms
class LoginForm (forms.Form):
   userid=forms.CharField(max_length=100)
