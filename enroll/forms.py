from django import forms
from .models import User




class RegistrationForm(forms.ModelForm):
    # Model form class
    class Meta:
        model=User
        fields=['username','email','password','firstname']

        help_texts={
            'username':'Input name here',
            'email':'Input Email here',
            'password':'Provide password here'
        }

        labels={
            'username':'Your Name',
            'email':'Your Email',
            'password':'Your Password'
        }
        
      
