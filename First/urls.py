from . import views
from django.urls import path
from .views import ProjListView,ProjDetailView,PostListView,PostDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.index,name='doki-index'),
    path('about/',views.about,name='doki-about'),
    path('contact/',views.contact,name='doki-contact'),
    path('project/',ProjListView.as_view(),name='doki-portfolio'),
    path('project/<int:pk>/',ProjDetailView.as_view(),name='proj_detail'),
	path('blog/',PostListView.as_view(),name='doki-blog'),
	path('blog/<int:pk>',PostDetailView.as_view(),name='post-detail'),
	path('practice/',views.practice,name='doki-practice'),
	path('example/',views.example,name='doki-example'),
	path('delete_project/<int:id>/',views.delete_project , name = 'delete_project'),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)