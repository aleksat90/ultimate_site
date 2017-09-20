from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from kalkulator import views

app_name = 'kalkulatorapp'

urlpatterns = [
    url(r'^app1/$', views.kalkulator_forma, name='kalkulator'),
    url(r'^rezultat/$', views.rezultat, name='rezultat')
]