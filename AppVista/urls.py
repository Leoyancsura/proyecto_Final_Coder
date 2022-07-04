from django.urls import path
from AppVista import views

urlpatterns = [
    path('',views.inicio, name='Inicio'),
]