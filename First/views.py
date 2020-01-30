from django.shortcuts import render

def about(request):
	return render(request, 'First/about.html')

def index(request):
	return render(request, 'First/index.html')

def blog(request):
	return render(request, 'First/blog.html')

def blogSingle(request):
	return render(request, 'First/blog-single.html')

def contact(request):
	return render(request, 'First/contact.html')

def portfolio(request):
	return render(request, 'First/portfolio.html')