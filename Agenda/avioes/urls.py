from django.urls import path
from .views import AviaoCreate, AviaoUpdate, AviaoDelete, AviaoList

urlpatterns = [
    path('avioes/', AviaoList.as_view(), name='listar-avioes'),
    path('avioes/criar/', AviaoCreate.as_view(), name='criar-aviao'),
    path('avioes/<int:pk>/edit/', AviaoUpdate.as_view(), name='editar-aviao'),
    path('avioes/<int:pk>/delete/', AviaoDelete.as_view(), name='excluir-aviao'),
]
