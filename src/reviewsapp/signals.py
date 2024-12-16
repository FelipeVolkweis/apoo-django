# reviewsapp/signals.py
"""
@file signals.py
@brief Arquivo que contém sinais para o aplicativo reviewsapp.

Este arquivo define um receptor de sinal para criar categorias iniciais após a migração do banco de dados.
"""
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Categoria

@receiver(post_migrate)
def create_initial_categorias(sender, **kwargs):
    """
    Função que cria categorias iniciais após a migração do banco de dados.

    Esta função é um receptor do sinal `post_migrate` e é executada após a migração
    do banco de dados. Se o remetente da migração for o aplicativo 'reviewsapp', 
    ela cria categorias iniciais predefinidas, se elas ainda não existirem no banco de dados.

    Args:
        sender (django.db.migrations.state.ProjectState): O remetente do sinal, que é o estado do projeto após a migração.
        **kwargs: Argumentos adicionais fornecidos pelo sinal.

    Categorias iniciais criadas:
        - Tecnologia
        - Saúde
        - Educação
        - Entretenimento
        - Esportes
    """
    if sender.name == 'reviewsapp':
        initial_categorias = ['Tecnologia', 'Saúde', 'Educação', 'Entretenimento', 'Esportes']
        for nome in initial_categorias:
            Categoria.objects.get_or_create(nome=nome)