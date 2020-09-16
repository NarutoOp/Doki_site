from . import views
from django.urls import path
from .views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.index,name='doki-index'),
    path('about/',views.about,name='doki-about'),
    path('contact/',views.contact,name='doki-contact'),
    path('portfolio/',views.portfolio,name='doki-portfolio'),
	path('blog/',views.blog,name='doki-blog'),
	path('blog-single/',views.blogSingle,name='doki-blog-single'),
	path('practice/',views.practice,name='doki-practice'),
	path('example/',views.example,name='doki-example'),
	path('delete_project/<int:id>/',views.delete_project , name = 'delete_project'),
    path('success', success, name = 'success'),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)