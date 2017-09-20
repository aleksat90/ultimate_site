"""pycharm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from blogapp import views
from kalkulator import views
from fUpload import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, kwargs='',name='admin'),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^home/$', TemplateView.as_view(template_name='index.html'), name='pocetna'),
    url(r'^blog/', include('blogapp.urls', namespace='blogapp')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^kalkulator/', include('kalkulator.urls', namespace='kalkulatorapp')),
    url(r'^charts/', include('charts.urls', namespace='chartapp')),
    url(r'^fupload/', include('fUpload.urls', namespace='fUploadapp')),
]
