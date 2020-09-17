from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from .models import project,post
from .forms import *

def about(request):
	return render(request, 'First/about.html')

def index(request):
	context = {
		'projects': project.objects.all(),
		'posts': post.objects.all()
	}
	return render(request, 'First/index.html',context)

def contact(request):
	return render(request, 'First/contact.html')


def practice(request):
	shows = project.objects.all()

	if request.method == 'POST':
		form = Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/practice')
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
		return redirect('/practice/')

def example(request):
	return render(request, 'First/example.html')


class ProjListView(ListView):
	model = project
	template_name = 'First/portfolio.html'
	context_object_name = 'projects'
	ordering = ['-date_posted']

class ProjDetailView(DetailView):
	model = project


class PostListView(ListView):
	model = post
	template_name = 'First/post.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = post