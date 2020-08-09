"""CrawlerProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from Crawler import views

router = routers.DefaultRouter()
router.register(r'platform', views.PlatformViewSet)
router.register(r'resource', views.ResourceViewSet)
router.register(r'manifest', views.ManifestViewSet)
router.register(r'config', views.ConfigViewSet)
#router.register(r'manifestsp', views.Manifest_SPViewSet)
router.register(r'news',views.NewsViewSet)
router.register(r'duration',views.DurationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]