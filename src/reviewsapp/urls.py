# reviewsapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_review, name='criar_review'),
    path('', views.lista_reviews, name='lista_reviews'),
    path('visualizar/<int:pk>/', views.visualizar_review, name='visualizar_review'), 
    path('editar/<int:pk>/', views.editar_review, name='editar_review'),             
    path('remover/<int:pk>/', views.remover_review, name='remover_review'),          
]
