from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("persona/create", views.persona_create, name="persona_create"),
    path('about/', views.about, name='about'),
]