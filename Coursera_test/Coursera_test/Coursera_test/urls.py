"""Coursera_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('home', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('about', views.about, name='about'),
    path('menu/grocessory', views.grocessory,name='grocessory'),
    path('menu/fruit_and_vegetable', views.fruit, name='fruit'),
    path('menu/giraj_product', views.giraj, name='giraj')

]+static(settings.STATIC_URL, document_root=settings.STATIC_URL)
