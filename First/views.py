from django.shortcuts import render

def about(request):
	return render(request, 'First/about.html',{'title': 'About'})