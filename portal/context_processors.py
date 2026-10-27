from .views import obter_menu


def menu_context(request):
    return {'menu_itens': obter_menu()}
