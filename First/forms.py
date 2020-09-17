from django import forms 
from .models import *
  
class Form(forms.ModelForm): 
  
    class Meta: 
        model = project 
        fields = ['title','project_img','content']

class Post_Form(forms.ModelForm): 
  
    class Meta: 
        model = post
        fields = ['title','post_img','content']