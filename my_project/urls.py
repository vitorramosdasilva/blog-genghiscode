from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('', include('blog.urls')),
    path('categoria/', include('categoria.urls')),
    path('admin/', admin.site.urls),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler50x = 'blog.views.error_500'
handler404 = 'blog.views.error_404'
handler403 = 'blog.views.error_403'
handler400 = 'blog.views.error_400'

# path('ckeditor/', include('ckeditor_uploader.urls')),
# path('', views.home, name='home'),
# path('post_details/<int:pk>/', views.post_details, name='post_details'),
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path('procura/<slug:slug>/', views.post_slug, name='post_slug'),
# path('procura/<content:content>', pesquisaView, name='pesquisa'),

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)