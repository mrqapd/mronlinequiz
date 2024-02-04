from django import forms
from django.contrib.auth.models import User
from . import models
from quiz import models as QMODEL

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput(attrs={'class':'form-control',  'placeholder' : 'Enter Your Password'}),
        'username':forms.TextInput(attrs={'class':'form-control',  'placeholder' : 'Enter Your Username'}),
        'last_name':forms.TextInput(attrs={'class':'form-control',  'placeholder' : 'Enter Your First Name' }),
        'first_name':forms.TextInput(attrs={'class':'form-control',  'placeholder' : 'Enter Your Last Name'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['address','mobile']
        widgets = {
            'address' : forms.TextInput(attrs={'class':'form-control',  'placeholder' : 'Enter Your ID '}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control',  'placeholder' : 'Enter Your Phone No.'}),
        }

