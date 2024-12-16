# reviewsapp/views.py

"""
@file views.py
@brief Este arquivo contém as views para o aplicativo de reviews.
Este arquivo define as funções de view para criar, listar, visualizar, editar e remover reviews no sistema. 
As views interagem com os modelos Review e Categoria, e utilizam formulários para manipulação dos dados.
@functions
    - criar_review(request): Cria uma nova review.
    - lista_reviews(request): Exibe uma lista de reviews filtrados por categoria, se fornecida.
    - visualizar_review(request, pk): Exibe os detalhes de uma review específica.
    - editar_review(request, pk): Edita uma review existente.
    - remover_review(request, pk): Remove uma review do sistema, marcando-a como deletada.
"""
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review, Categoria
from django.contrib import messages

def criar_review(request):
    """
    Cria uma nova review.
    Este view lida com a criação de uma nova review. Se o método da requisição for POST,
    ele tenta validar e salvar o formulário de review. Se o formulário for válido, a review
    é salva e uma mensagem de sucesso é exibida. Caso contrário, uma mensagem de erro é exibida.
    Se o método da requisição não for POST, um formulário vazio é exibido.
    Args:
        request (HttpRequest): O objeto da requisição HTTP.
    Returns:
        HttpResponse: A resposta HTTP com o formulário de review renderizado.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review criada com sucesso!')
            return redirect('lista_reviews')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'review': None,
    }
    return render(request, 'reviews/review_form.html', context)

def lista_reviews(request):
    """
    Exibe uma lista de reviews filtrados por categoria, se fornecida.
    Args:
        request (HttpRequest): O objeto de solicitação HTTP.
    Returns:
        HttpResponse: A resposta HTTP com a renderização da página de lista de reviews.
    Variáveis:
        categoria_id (int): O ID da categoria selecionada, se fornecida.
        reviews (QuerySet): O conjunto de reviews filtrados.
        categorias (QuerySet): O conjunto de categorias disponíveis.
        context (dict): O contexto a ser passado para o template.
    Tratamento de Erros:
        ValueError: Capturado se o ID da categoria fornecido não for um número inteiro válido.

            """
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        try:
            categoria_id = int(categoria_id)
            reviews = Review.objects.filter(categoria__id=categoria_id, data_delecao__isnull=True).order_by('-data_criacao')
        except ValueError:
            messages.error(request, 'Categoria inválida selecionada.')
            reviews = Review.objects.filter(data_delecao__isnull=True).order_by('-data_criacao')
    else:
        reviews = Review.objects.filter(data_delecao__isnull=True).order_by('-data_criacao')
    
    categorias = Categoria.objects.filter(data_delecao__isnull=True)
    
    context = {
        'reviews': reviews,
        'categorias': categorias,
        'categoria_selecionada': categoria_id,
    }
    return render(request, 'reviews/review_list.html', context)

def visualizar_review(request, pk):
    """
    Exibe os detalhes de uma review específica.

    Esta função busca uma review pelo seu identificador primário (pk) e garante que a review não tenha sido deletada (data_delecao é nula). 
    Em seguida, renderiza a página de detalhes da review.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.
        pk (int): O identificador primário da review a ser visualizada.

    Returns:
        HttpResponse: A resposta HTTP com a página de detalhes da review renderizada.

    Raises:
        Http404: Se a review não for encontrada ou se tiver sido deletada.
    """
    review = get_object_or_404(Review, pk=pk, data_delecao__isnull=True)
    context = {
        'review': review
    }
    return render(request, 'reviews/review_detail.html', context)

def editar_review(request, pk):
    """
    Edita uma review existente.
    Esta função lida com a edição de uma review específica identificada pelo seu ID (pk).
    Se o método da requisição for POST, ela tenta salvar as alterações feitas no formulário.
    Se o formulário for válido, a review é salva e uma mensagem de sucesso é exibida.
    Caso contrário, uma mensagem de erro é exibida.
    Se o método da requisição não for POST, o formulário é exibido com os dados atuais da review.
    Args:
        request (HttpRequest): O objeto da requisição HTTP.
        pk (int): O ID primário da review a ser editada.
    Returns:
        HttpResponse: A resposta HTTP que renderiza o template 'reviews/review_form.html' com o formulário e a review.
    """
    review = get_object_or_404(Review, pk=pk, data_delecao__isnull=True)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review atualizada com sucesso!')
            return redirect('lista_reviews')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'reviews/review_form.html', context)

def remover_review(request, pk):
    """
    Remove uma review do sistema, marcando-a como deletada.

    Este método busca uma review pelo seu identificador primário (pk) e verifica se ela não foi deletada anteriormente.
    Se a requisição for do tipo POST, a review é marcada como deletada e o usuário é redirecionado para a lista de reviews
    com uma mensagem de sucesso. Caso contrário, é exibida uma página de confirmação de deleção.

    Args:
        request (HttpRequest): O objeto da requisição HTTP.
        pk (int): O identificador primário da review a ser removida.

    Returns:
        HttpResponse: A resposta HTTP com a página de confirmação de deleção ou redirecionamento após a deleção.
    """
    review = get_object_or_404(Review, pk=pk, data_delecao__isnull=True)
    if request.method == 'POST':
        review.soft_delete()
        messages.success(request, 'Review removida com sucesso!')
        return redirect('lista_reviews')
    context = {
        'review': review
    }
    return render(request, 'reviews/review_confirm_delete.html', context)
