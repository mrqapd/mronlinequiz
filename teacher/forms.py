from django import forms
from django.contrib.auth.models import User
from . import models

#attrs={'class':'form-control', 'placeholder' : 'Enter Your Password'
#attrs={'class':'form-control', 'style':'width: 480px; height: 65.26px; left: 0px; top: 52.60px; position: absolute; background: #D9D9D9; box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.25); border-radius: 13px', 'placeholder' : 'Enter Your Password'
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control', }),
        'last_name':forms.TextInput(attrs={'class':'form-control',  }),
        'first_name':forms.TextInput(attrs={'class':'form-control',}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model=models.Teacher
        fields=['address','mobile']
        widgets = {
            'address' : forms.TextInput(attrs={'class':'form-control',}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control'}),
        }

