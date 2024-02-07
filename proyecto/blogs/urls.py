from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
    path('create/', views.create_blog, name='blog_create'),
    path('blog/<int:blog_id>/', views.detalle_blog, name='detalle_blog'),
]

