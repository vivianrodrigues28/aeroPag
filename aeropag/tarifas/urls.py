from django.urls import path
from . import views  # Adicione esta linha para importar as views

from .views import TarifaCreate, TarifaUpdate, TarifaDelete, TarifaList

urlpatterns = [
    # Listar tarifas
    path('tarifas/', TarifaList.as_view(), name='listar-tarifas'),
    
    # Criar tarifa
    path('tarifas/criar/', TarifaCreate.as_view(), name='criar-tarifa'),
    
    # Editar tarifa
    path('tarifas/<int:pk>/edit/', TarifaUpdate.as_view(), name='editar-tarifa'),
    
    # Excluir tarifa
    path('tarifas/<int:pk>/delete/', TarifaDelete.as_view(), name='deletar-tarifa'),
]
