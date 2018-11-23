"""cupofsea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.postdetails, name='postdetails'),
    path('blog/speaking/new', views.speaking_log, name='speaking_log'),
    path('blog/listening/new', views.listening_log, name='listening_log'),
    path('blog/writing/new', views.writing_log, name='writing_log'),
    path('blog/reading/new', views.reading_log, name='reading_log'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)