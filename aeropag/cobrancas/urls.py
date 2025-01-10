from django.urls import path
from .views import CobrancaList, CobrancaCreate, CobrancaUpdate, CobrancaDelete

urlpatterns = [
    path('cobrancas/listar/',CobrancaList, name='listar_cobrancas'),
    path('cobranca/nova/', CobrancaCreate, name='criar_cobranca'),
    path('cobranca/<int:id>/editar/', CobrancaUpdate, name='atualizar_cobranca'),
    path('cobranca/<int:id>/excluir/', CobrancaDelete, name='excluir_cobranca'),
]
