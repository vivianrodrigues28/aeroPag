from django.urls import path
from .views import ClienteCreate, ClienteUpdate, ClienteDelete, ClienteList

urlpatterns = [
    # Listar clientes
    path('clientes/', ClienteList.as_view(), name='listar-clientes'),
    
    # Criar cliente
    path('clientes/criar/', ClienteCreate.as_view(), name='criar-cliente'),
    
    # Editar cliente
    path('clientes/<int:pk>/edit/', ClienteUpdate.as_view(), name='editar-cliente'),
    
    # Excluir cliente
    path('clientes/<int:pk>/delete/', ClienteDelete.as_view(), name='excluir-cliente'),

]
