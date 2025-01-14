from django.urls import path
from .views import AviaoCreate, AviaoUpdate, AviaoDelete, AviaoList, editar_aviao, excluir_aviao

urlpatterns = [
    path('avioes/', AviaoList.as_view(), name='listar-avioes'),
    path('avioes/criar/', AviaoCreate.as_view(), name='criar-aviao'),
    path('avioes/<int:pk>/edit/', editar_aviao, name='editar-aviao'),  
    path('avioes/<int:pk>/excluir/', excluir_aviao, name='excluir_aviao'), 
    
]
