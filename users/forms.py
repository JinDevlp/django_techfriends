from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User 
from .models import Profile

class SignupForm(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ('username','email','password1','password2')
        
   

class ProfileForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ('first_name','last_name','email','bio','profile_image','github','linkedin','portfolio')
        
   

class EditProfileForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User 
        fields = ('username','first_name','last_name',
                 'email')