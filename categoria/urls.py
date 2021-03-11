from django.urls import path
from categoria import views
from categoria.views import CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('post_category/<int:pk>/', views.category, name='post_category'),
    path('category/new/', CategoryCreateView, name='category-create'),
    path('category/<int:pk>/update/', CategoryUpdateView, name='category-update'),
    path('category/<int:pk>/delete/', CategoryDeleteView, name='category-delete'),
]
