from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.
from my_app.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_details(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(request, 'post_details.html', {'posts': posts})
