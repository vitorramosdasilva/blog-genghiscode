from django.urls import path

from . import views

urlpatterns = [
    # path('', views.BlogListView.as_view(), name='home'),
    # path('post/teste/', views.hello, name='hello'),
    # path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('', views.BlogListView.as_view(), name='home'),
    path('', views.home, name='home'),
    path('post_details/<int:pk>/', views.post_details, name='post_details'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

]
