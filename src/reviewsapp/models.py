"""
@file models.py
@brief Este arquivo contém as definições dos modelos Categoria e Review para o sistema de avaliações.
"""
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Categoria(models.Model):
    """
    Classe Categoria que representa uma categoria no sistema.
    Atributos:
        nome (CharField): Nome da categoria com um tamanho máximo de 100 caracteres.
        data_criacao (DateTimeField): Data e hora de criação da categoria, preenchida automaticamente.
        data_edicao (DateTimeField): Data e hora da última edição da categoria, preenchida automaticamente.
        data_delecao (DateTimeField): Data e hora de deleção da categoria, pode ser nula e possui índice no banco de dados.
    Métodos:
        __str__(): Retorna o nome da categoria como sua representação em string.
        soft_delete(): Marca a categoria como deletada preenchendo o campo data_delecao com a data e hora atual.
        restore(): Restaura a categoria removendo a data de deleção.
    Meta:
        db_table: Nome da tabela no banco de dados.
        verbose_name: Nome legível da categoria.
        verbose_name_plural: Nome legível no plural das categorias.
    """
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
    """
    Classe Review representa uma avaliação no sistema.
    Atributos:
        titulo (CharField): Título da avaliação, com no máximo 100 caracteres.
        conteudo (TextField): Conteúdo da avaliação.
        nota (IntegerField): Nota da avaliação, com valor mínimo de 1 e máximo de 10.
        data_criacao (DateTimeField): Data e hora de criação da avaliação, preenchida automaticamente.
        data_edicao (DateTimeField): Data e hora da última edição da avaliação, preenchida automaticamente.
        data_delecao (DateTimeField): Data e hora de deleção lógica da avaliação, pode ser nula.
        categoria (ForeignKey): Categoria associada à avaliação, pode ser nula.
    Métodos:
        __str__(): Retorna o título da avaliação.
        soft_delete(): Realiza a deleção lógica da avaliação, preenchendo o campo data_delecao com a data e hora atual.
        restore(): Restaura a avaliação deletada logicamente, definindo o campo data_delecao como None.
    Meta:
        db_table: Nome da tabela no banco de dados.
        verbose_name: Nome legível da classe.
        verbose_name_plural: Nome legível no plural da classe.
    """
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