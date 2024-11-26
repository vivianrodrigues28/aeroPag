from django.urls import path
from . import views 
from .views import ClienteCreate, ClienteUpdate, ClienteDelete, ClienteList, editar_cliente

urlpatterns = [
    
    path('clientes/', ClienteList.as_view(), name='listar-clientes'),
    path('clientes/criar/', ClienteCreate.as_view(), name='criar-cliente'),
    path('clientes/<int:pk>/edit/', ClienteUpdate.as_view(), name='editar-cliente'),

    path('clientes/<int:pk>/edit/', views.editar_cliente, name='editar-cliente'),
    
    path('clientes/<int:pk>/delete/', ClienteDelete.as_view(), name='excluir-cliente'),

]
