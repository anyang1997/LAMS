"""LAMS URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.views import serve

from timetable import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('about/', views.about, name='about'),
    path('manage/', views.manage, name='manage'),
    path('inquire/', views.inquire, name='inquire'),
    path('book/', views.book, name='book'),
    path('get_week_ord/', views.get_week_ord, name='get_week_ord'),
    path('admin/', admin.site.urls, name='admin'),
    path('favicon.ico', serve, {'path': 'images/favicon.ico'}),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
