from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog/<str:blog_id>/', views.blog, name='blog_page')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)