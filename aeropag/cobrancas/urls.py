from django.urls import path
from .views import CobrancaList, CobrancaCreate, CobrancaUpdate, CobrancaDelete, CobrancaDetails

urlpatterns = [
    path('cobranca/', CobrancaList, name='listar_cobrancas'),  
    path('cobranca/nova/', CobrancaCreate, name='criar_cobranca'),
    path('cobranca/<int:id>/editar/', CobrancaUpdate, name='atualizar_cobranca'),
    path('cobranca/<int:id>/excluir/', CobrancaDelete, name='excluir_cobranca'),
    path('cobranca/<int:id>/', CobrancaDetails, name='detalhes_cobranca'),
]
