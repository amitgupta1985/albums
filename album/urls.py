"""album URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from category import views
from Auth.views import LoginAPIView, LogoutAPIView, RegisterAPIView
from gallery import views as galleryview
from category import views as cateView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/v1/user/category/', include('category.api_urls')),
    path('api/v1/category/', cateView.categList),
    path('api/v1/user/gallery/', include('gallery.api_urls')),
    path('api/v1/gallery/', galleryview.gallerylist),
    path('api/v1/gallery/<int:id>/', galleryview.detail),
    path('api/v1/gallery/category/<int:category_id>/', galleryview.getByCategory),
    path('api/v1/user/register',RegisterAPIView.as_view()),
    path('api/v1/auth/login', LoginAPIView.as_view()),
    path('api/v1/auth/logout', LogoutAPIView.as_view())
]
