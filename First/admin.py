from django.contrib import admin
from .models import project,post

myModels = [project,post]

admin.site.register(myModels)
