# reviewsapp/forms.py
"""
@file forms.py
@brief Formulários para criação e edição de avaliações.

Este arquivo contém a definição do formulário baseado no modelo Review.
"""
from django import forms
from .models import Review, Categoria

class ReviewForm(forms.ModelForm):
    """
    Formulário para criação e edição de avaliações.

    Classes:
        ReviewForm: Formulário baseado no modelo Review.

    Atributos:
        Meta:
            model (Review): Modelo associado ao formulário.
            fields (list): Campos do modelo que serão utilizados no formulário.
            widgets (dict): Widgets personalizados para os campos do formulário.
            labels (dict): Rótulos personalizados para os campos do formulário.

    Campos:
        titulo (str): Título da avaliação.
        categoria (str): Categoria da avaliação.
        conteudo (str): Conteúdo da avaliação.
        nota (int): Nota da avaliação, variando de 1 a 10.
    """
    class Meta:
        model = Review
        fields = ['titulo', 'categoria', 'conteudo', 'nota']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
        }
        labels = {
            'titulo': 'Título',
            'categoria': 'Categoria',
            'conteudo': 'Conteúdo',
            'nota': 'Nota',
        }
