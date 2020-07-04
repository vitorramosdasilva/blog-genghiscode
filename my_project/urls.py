"""my_project url configuration

the `urlpatterns` list routes urls to views. for more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
examples:
function views
    1. add an import:  from my_app import views
    2. add a url to urlpatterns:  path('', views.home, name='home')
class-based views
    1. add an import:  from other_app.views import home
    2. add a url to urlpatterns:  path('', home.as_view(), name='home')
including another urlconf
    1. import the include() function: from django.urls import include, path
    2. add a url to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from my_app import views
# from my_app.views import pesquisaView
# from . views import pesquisaView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('post_details/<int:pk>/', views.post_details, name='post_details'),
                  path('category/<int:pk>/', views.category, name='category'),
                  path('pesquisa/', views.pesquisa, name='pesquisa'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler50x = 'my_app.views.error_500'
handler404 = 'my_app.views.error_404'
handler403 = 'my_app.views.error_403'
handler400 = 'my_app.views.error_400'

# path('procura/<slug:slug>/', views.post_slug, name='post_slug'),
# path('procura/<content:content>', pesquisaView, name='pesquisa'),
