# reviewsapp/forms.py

from django import forms
from .models import Review, Categoria

class ReviewForm(forms.ModelForm):
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
