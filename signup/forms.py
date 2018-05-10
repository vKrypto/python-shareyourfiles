#-*- coding: utf-8 -*-
from django import forms


class Form1(forms.Form):
   fname = forms.CharField(max_length = 100)
   lname = forms.CharField(max_length = 100)
   email = forms.CharField(max_length = 100)
   ph = forms.IntegerField()

class Form3(forms.Form):
   desig=forms.CharField(max_length=100)
   org=forms.CharField(max_length=100)

class Form4(forms.Form):
   passwd=forms.CharField(max_length=100)

class Choose_pic(forms.Form):
   pic=forms.ImageField()