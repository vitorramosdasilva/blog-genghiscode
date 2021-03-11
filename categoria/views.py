from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Category
from .forms import CategoryForm
from django.contrib import messages


def category(request, pk):
    categoria = Category.objects.get(pk=pk)
    context = {
        'category': categoria,
        'posts': Post.objects.filter(category=categoria),
    }
    return render(request, 'post_category.html', context)


@login_required
def CategoryCreateView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.author = request.user
            categoria.save()
            return redirect('blog-home')

    else:
        form = CategoryForm()
    return render(request, 'categoria/category_create.html', {'form': form})


@login_required
def CategoryUpdateView(request, pk):
    categoria = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=categoria)
        if form.is_valid():
            if request.user == categoria.author:
                categoria = form.save(commit=False)
                categoria.author = request.user
                categoria.save()
                return redirect('blog-home')
    else:
        form = CategoryForm(instance=categoria)
    return render(request, 'categoria/category_edit.html', {'form': form})


@login_required
def CategoryDeleteView(request, pk):
    categoria = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=categoria)
        if form.is_valid():
            if request.user == categoria.author:
                categoria.delete()
                messages.success(request, 'Category delete successfully')
                return redirect('blog-home')
    else:
        form = CategoryForm(instance=categoria)
    return render(request, 'categoria/category_delete.html', {'form': form, 'category': categoria})