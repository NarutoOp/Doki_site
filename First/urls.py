from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.index,name='doki-index'),
    path('about/',views.about,name='doki-about'),
    path('contact/',views.contact,name='doki-contact'),
    path('portfolio/',views.portfolio,name='doki-portfolio'),
	path('blog/',views.blog,name='doki-blog'),
	path('blog-single/',views.blogSingle,name='doki-blog-single'),
	path('practice/',views.practice,name='doki-practice'),
	path('example/',views.example,name='doki-example'),
]
