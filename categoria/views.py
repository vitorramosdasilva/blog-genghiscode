from django.shortcuts import render
from blog.models import Post, Category
# from categoria.forms import Categoryform
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


def category(request, pk):
    categoria = Category.objects.get(pk=pk)
    context = {
        'category': categoria,
        'posts': Post.objects.filter(category=categoria),
    }
    return render(request, 'post_category.html', context)


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'categoria/home.html'
#
#
# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = 'categoria/category_detail.html'
#
#
# class CategoryCreateView(SuccessMessageMixin, CreateView):
#     model = Category
#     template_name = 'categoria/category_new.html'
#     form_class = Categoryform
#     success_message = "%(field)s - criado com sucesso"
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.autor = self.request.user
#         obj.save()
#         return super().form_valid(form)
#
#     def get_success_message(self, cleaned_data):
#         return self.success_message % dict(
#             cleaned_data,
#             field=self.object.titulo,
#         )
#
# # class PostUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
#
#
# class CategoryUpdateView(SuccessMessageMixin, UpdateView):
#     model = Category
#     form_class = Categoryform
#     template_name = 'categoria/category_edit.html'
#     # fields = ('summary','content')
#     success_message = "%(field)s - alterado com sucesso"
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.autor = self.request.user
#         obj.save()
#         return super().form_valid(form)
#
#     def get_success_message(self, cleaned_data):
#         return self.success_message % dict(
#             cleaned_data,
#             field=self.object.titulo,
#         )
#
# # class PostDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
#
#
# class CategoryDeleteView(SuccessMessageMixin, DeleteView):
#     model = Category
#     template_name = 'categoria/category_delete.html'
#     success_url = reverse_lazy('home')
#     success_message = "Deletado com sucesso"
#
#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_message)
#         return super(CategoryDeleteView, self).delete(request, *args, **kwargs)
