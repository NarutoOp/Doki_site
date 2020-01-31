from django.shortcuts import render
from .models import Project

def about(request):
	return render(request, 'First/about.html')

def index(request):
	context = {
		'posts': Project.objects.all()
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
	return render(request, 'First/practice.html')

def example(request):
	return render(request, 'First/example.html')