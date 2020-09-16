from django.http import HttpResponse 
from django.shortcuts import render, redirect
from .models import project
from .forms import *

def about(request):
	return render(request, 'First/about.html')

def index(request):
	context = {
		'posts': project.objects.all()
	}
	return render(request, 'First/index.html',context)
	
def blog(request):
	return render(request, 'First/blog.html')

def blogSingle(request):
	return render(request, 'First/blog-single.html')

def contact(request):
	return render(request, 'First/contact.html')

def portfolio(request):
	return render(request, 'First/portfolio.html')

def practice(request):
	shows = project.objects.all()

	if request.method == 'POST':
		form = Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = Form()
	return render(request, 'First/practice.html',{
		'shows' : shows,
		'form' : form
	})

def delete_project(request, id):
	if request.method == 'POST':
		proj = project.objects.get(id=id)
		proj.delete()
		return redirect('success')

def example(request):
	return render(request, 'First/example.html')  
  
def success(request):
	HttpResponse('successfully uploaded')
	return redirect('practice/')