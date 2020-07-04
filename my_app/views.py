from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.
from my_app.forms import PesquisaForm
from my_app.models import Post, Category


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_slug(request, slug):
    posts = Post.objects.get(slug=slug)
    context = {
        'posts': posts
    }
    return render(request, 'catalog/product.html', context)


def post_details(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(request, 'post_details.html', {'posts': posts})


def category(request, pk):
    categoria = Category.objects.get(pk=pk)
    context = {
        'category': categoria,
        'posts': Post.objects.filter(category=categoria),
    }
    return render(request, 'category.html', context)


def pesquisa(request):
    # success = False
    form = PesquisaForm(request.POST or None)
    if form.is_valid():
        procura = form.cleaned_data['pesquisa']
        posts = Post.objects.filter(content__contains=procura)
    context = {
        'form': form,
        'posts': posts,
    }
    return render(request, 'home.html', context)


def error_400(request, exception):
    return render(request, '400.html', status=400)


def error_403(request, exception):
    return render(request, '403.html', status=403)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_50x(request, exception):
    return render(request, '500.html', status=500)
