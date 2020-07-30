from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .forms import PesquisaForm, Postform
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


# def post_slug(request, slug):
#     posts = Post.objects.get(slug=slug)
#     context = {
#         'posts': posts
#     }
#     return render(request, 'catalog/product.html', context)


def post_details(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(request, 'blog/post_details.html', {'posts': posts})

# class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):


class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    form_class = Postform
    success_message = "%(field)s - criado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

# class PostUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):


class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = Postform
    template_name = 'blog/post_edit.html'
    # fields = ('summary','content')
    success_message = "%(field)s - alterado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

# class PostDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):


class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)


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


def error_400(request, exception):
    return render(request, '400.html', status=400)


def error_403(request, exception):
    return render(request, '403.html', status=403)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_50x(request, exception):
    return render(request, '500.html', status=500)
