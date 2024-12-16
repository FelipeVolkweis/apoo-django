# reviewsapp/urls.py
"""
@file urls.py
@brief Padrões de URL para o aplicativo reviewsapp.

Este módulo define os padrões de URL para o aplicativo reviewsapp.

Padrões de URL:
- 'criar/': Mapeia para a view `criar_review` para criar uma nova review.
- '': Mapeia para a view `lista_reviews` para listar todas as reviews.
- 'visualizar/<int:pk>/': Mapeia para a view `visualizar_review` para visualizar uma review específica.
- 'editar/<int:pk>/': Mapeia para a view `editar_review` para editar uma review específica.
- 'remover/<int:pk>/': Mapeia para a view `remover_review` para remover uma review específica.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_review, name='criar_review'),
    path('', views.lista_reviews, name='lista_reviews'),
    path('visualizar/<int:pk>/', views.visualizar_review, name='visualizar_review'), 
    path('editar/<int:pk>/', views.editar_review, name='editar_review'),             
    path('remover/<int:pk>/', views.remover_review, name='remover_review'),          
]
