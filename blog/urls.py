from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('access', views.access, name='access'),
    path('line', views.line, name='line'),
    path('blog', views.blog, name='blog'),
]