from django.urls import path, include
from categoria import views
from django.conf import settings
from django.conf.urls.static import static
# from categoria.views import CategoryListView
from django.contrib import admin

urlpatterns = [
    path('post_category/<int:pk>/', views.category, name='post_category'),
    # path('', CategoryListView.as_view, name='category_home'),
    # path('category_details/<int:pk>/', views.Category_details, name='post_details'),
    # path('category/new/', views.CategoryCreateView.as_view(), name='post_new'),
    # path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='post_edit'),
    # path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='post_delete'),
]
