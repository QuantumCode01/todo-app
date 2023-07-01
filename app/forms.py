from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.exceptions import ValidationError 







class TaskForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add new task.....'}))
    class Meta:
        model=Task
        fields = ['name','title','complete']
        widgets={
            'complete':forms.CheckboxInput(attrs={'class':'form-check-input','onclick':'this.form.submit();'}),
          }
        
        
   
        
             
    
class UserRegisterationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            }   
    

  
    def clean(self):  
        cleaned_data=super().clean() 
    
        email = self.cleaned_data['email'].lower() 
        new = User.objects.filter(email=email)    
        if new.count():  
            raise ValidationError(" Email Already Exist") 
        
       
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
       

    # def save(self, commit = True):  
    #     user = User.objects.create_user(  
    #         self.cleaned_data['username'],  
    #         self.cleaned_data['email'],  
    #         self.cleaned_data['password1']  
    #     )  
    #     return user  
        
        
class UserAuthenticationForm(AuthenticationForm):
   password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
   username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))  