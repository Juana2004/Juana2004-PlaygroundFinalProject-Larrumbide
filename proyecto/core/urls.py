from django.urls import path
from . import views
from .views import index, persona_create

urlpatterns = [
    path("", views.index, name="index"),
    path("persona/create", views.persona_create, name="persona_create"),
    path('about/', views.about, name='about'),
]