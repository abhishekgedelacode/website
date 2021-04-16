from django.urls import path
from . import views

app_name = 'land'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts, name='posts'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('comments/', views.comments, name='comments'),
    path('info/', views.info, name='info'),
]
