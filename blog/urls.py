from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, \
    CommentDeleteView, CommentUpdateView

# app_name = 'blog'
urlpatterns = [
    # path('', home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/new/', PostCreateView, name='post-create'),

    path('post/<int:pk>/update', PostUpdateView, name='post-update'),
    path('comment/<int:pk>/update', CommentUpdateView, name='comment-update'),

    path('post/<int:pk>/delete', PostDeleteView, name='post-delete'),
    path('comment/<int:pk>/delete', CommentDeleteView, name='comment-delete')


]