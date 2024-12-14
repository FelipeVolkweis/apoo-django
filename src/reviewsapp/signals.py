# reviewsapp/signals.py

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Categoria

@receiver(post_migrate)
def create_initial_categorias(sender, **kwargs):
    if sender.name == 'reviewsapp':
        initial_categorias = ['Tecnologia', 'Saúde', 'Educação', 'Entretenimento', 'Esportes']
        for nome in initial_categorias:
            Categoria.objects.get_or_create(nome=nome)