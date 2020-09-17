from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from .models import project,post
from .forms import *
from django.contrib.auth.decorators import user_passes_test


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

@user_passes_test(lambda u: u.is_superuser)
def projForm(request):
	shows = project.objects.all()

	if request.method == 'POST':
		form = Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/proj_form')
	else:
		form = Form()
	return render(request, 'First/proj_form.html',{
		'shows' : shows,
		'form' : form
	})

@user_passes_test(lambda u: u.is_superuser)
def postForm(request):
	shows = post.objects.all()

	if request.method == 'POST':
		post_form = Post_Form(request.POST, request.FILES)
		if post_form.is_valid():
			post_form.save()
			return redirect('/post_form')
	else:
		post_form = Post_Form()
	return render(request, 'First/post_form.html',{
		'shows' : shows,
		'form' : post_form
	})

@user_passes_test(lambda u: u.is_superuser)
def delete_project(request, id):
	if request.method == 'POST':
		proj = project.objects.get(id=id)
		proj.delete()
		return redirect('/proj_form/')

@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, id):
	if request.method == 'POST':
		pos = post.objects.get(id=id)
		pos.delete()
		return redirect('/post_form/')

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