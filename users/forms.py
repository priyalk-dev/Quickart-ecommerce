from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    
    password2 =forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    
    
    class Meta:
        model= User
        fields = ['username','email','password1','password2']      
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
           
        }   
        
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'})
            self.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'})
            
            
            
    def clean(self):
            cleaned_data =super().clean()
            password1=cleaned_data.get('password1')
            password2=cleaned_data.get('password2')
            
            if password1 and password2 and password1!=password2:
                return ValidationError("Password do not match")
            return cleaned_data

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))