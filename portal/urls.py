from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conteudo/<slug:slug>/', views.exibir_conteudo, name='exibir_conteudo'),
]
