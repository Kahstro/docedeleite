from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo-doce/', views.novoDoce, name='novoDoce'),
    path('leite-com-goiaba/', views.leiteGoiaba, name='leiteGoiaba'),
    path('ainda-tem-doce/', views.aindaTem, name='aindaTem'),
]