# reviewsapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review, Categoria
from django.contrib import messages

def criar_review(request):
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
    review = get_object_or_404(Review, pk=pk, data_delecao__isnull=True)
    context = {
        'review': review
    }
    return render(request, 'reviews/review_detail.html', context)

def editar_review(request, pk):
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
    review = get_object_or_404(Review, pk=pk, data_delecao__isnull=True)
    if request.method == 'POST':
        review.soft_delete()
        messages.success(request, 'Review removida com sucesso!')
        return redirect('lista_reviews')
    context = {
        'review': review
    }
    return render(request, 'reviews/review_confirm_delete.html', context)
