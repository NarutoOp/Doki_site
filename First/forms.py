from django import forms 
from .models import *
  
class Form(forms.ModelForm): 
  
    class Meta: 
        model = project 
        fields = ['title','project_img'] 