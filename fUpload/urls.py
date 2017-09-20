from django.conf.urls import url, include
from django.contrib import admin
from fUpload import views

app_name = 'fUploadapp'

urlpatterns = [
    url(r'^fupload/$', views.fUpload, name='file_upload'),
    url(r'^lista_fajlova/', views.FajloviListView.as_view(), name='lista_fajlova'),
]