from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, CommentDeleteView

# app_name = 'blog'
urlpatterns = [
    # path('', home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/new/', PostCreateView, name='post-create'),

    path('post/<int:pk>/update', PostUpdateView, name='post-update'),
    path('comment/<int:pk>/update', PostUpdateView, name='post-comment'),

    path('post/<int:pk>/delete', PostDeleteView, name='post-delete'),
    path('comment/<int:pk>/delete', CommentDeleteView, name='comment-delete')


]