from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from charts import views

app_name = 'chartapp'

urlpatterns = [
    url(r'^chart/$', views.chartView, name='chart'),
]