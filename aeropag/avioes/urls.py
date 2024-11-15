from django.urls import path
from .views import AviaoCreate, AviaoUpdate, AviaoDelete, AviaoList, editar_aviao, excluir_aviao

urlpatterns = [
    path('avioes/', AviaoList.as_view(), name='listar-avioes'),
    path('avioes/criar/', AviaoCreate.as_view(), name='criar-aviao'),
    path('avioes/<int:pk>/edit/', editar_aviao, name='editar-aviao'),  # Usando 'pk' agora
    path('avioes/<int:pk>/delete/', excluir_aviao, name='excluir-aviao'),  # Usando 'pk' agora
    
]
