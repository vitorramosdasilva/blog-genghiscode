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
    # Social ...
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler50x = 'blog.views.error_500'
handler404 = 'blog.views.error_404'
handler403 = 'blog.views.error_403'
handler400 = 'blog.views.error_400'


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)