from django.shortcuts import get_object_or_404, render
from .models import Conteudo, Menu


def obter_menu():
    """Retorna os itens ativos do menu, ordenados, com o conteúdo já carregado."""
    return (
        Menu.objects.filter(ativo=True)
        .select_related('conteudo')
        .order_by('ordem')
    )


def index(request):
    capa = Conteudo.objects.filter(slug='inicio', ativo=True).first()
    return render(request, 'portal/index.html', {'conteudo': capa})


def exibir_conteudo(request, slug):
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, 'portal/conteudo.html', {'conteudo': conteudo})
