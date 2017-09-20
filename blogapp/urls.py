from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    url(r'^new_post/$', views.KreirajPostView.as_view(), name='create_post'),
    url(r'^post_list/$', views.ListaPostovaView.as_view(), name='lista_postova'),
    url(r'^post/(?P<pk>\d+)$', views.DetaljPostaView.as_view(), name='post_pojedinacan'),
    url(r'^about_me/$', views.AboutMeView.as_view(), name='about_me')
]