"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('biography.urls')),
    path('api/v2/', include('certificate.urls')),
    path('api/v3/', include('comment.urls')),
    path('api/v4/', include('contact.urls')),
    path('api/v5/', include('portfolio.urls')),
    path('api/v6/', include('skills.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
