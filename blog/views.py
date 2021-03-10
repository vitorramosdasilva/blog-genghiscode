from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.
from blog.forms import PesquisaForm, PostForm, CommentForm
from blog.models import Post, Comment
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404


# @login_required
def pesquisa(request):
    # success = False
    if request.method == 'GET':
        form = PesquisaForm()
        return render(request, "blog/home.html", {'form': form})
    else:
        form = PesquisaForm(request.POST)
        if form.is_valid():
            procura = form.cleaned_data['pesquisa']
            posts = Post.objects.filter(content__icontains=procura)
            context = {
                'form': form,
                'posts': posts,
            }
        return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5


@login_required
def PostDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = CommentForm()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form_comment': form,
                                                     'new_coment': new_comment,
                                                     'post': post,
                                                     'comments': comments
                                                     })


@login_required
def PostCreateView(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-detail', pk=post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


@login_required
def PostUpdateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            if request.user == post.author:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def CommentUpdateView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post.pk
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            if request.user == comment.author:
                comment = form.save(commit=False)
                comment.author = request.user
                comment.save()
                return redirect('post-detail', pk=post)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form})


@login_required
def PostDeleteView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            if request.user == post.author:
                Post.delete()
                messages.success(request, 'Post delete successfully')
                return redirect('blog-home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_delete.html', {'form': form})


@login_required
def CommentDeleteView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            if request.user == comment.author:
                comment.delete()
                messages.success(request, 'Comentário deletado com sucesso')
                return redirect('blog-home')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_delete.html', {'form': form})


def error_400(request, exception):
    return render(request, 'erro/400.html', status=400)


def error_403(request, exception):
    return render(request, 'erro/403.html', status=403)


def error_404(request, exception):
    return render(request, 'erro/404.html', status=404)


def error_50x(request, exception):
    return render(request, 'erro/500.html', status=500)
