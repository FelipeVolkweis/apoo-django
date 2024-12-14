from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)
    data_delecao = models.DateTimeField(null=True, blank=True, db_index=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def soft_delete(self):
        self.data_delecao = timezone.now()
        self.save()
    
    def restore(self):
        self.data_delecao = None
        self.save()

class Review(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    nota = models.IntegerField(
        validators=[
            MinValueValidator(1, message="A nota mínima é 1."),
            MaxValueValidator(10, message="A nota máxima é 10.")
        ]
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_edicao = models.DateTimeField(auto_now=True)
    data_delecao = models.DateTimeField(null=True, blank=True, db_index=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def soft_delete(self):
        self.data_delecao = timezone.now()
        self.save()
    
    def restore(self):
        self.data_delecao = None
        self.save()