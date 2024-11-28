from django.urls import path
from . import views  

from .views import TarifaCreate, TarifaUpdate, TarifaDelete, TarifaList

urlpatterns = [
    
    path('tarifas/', TarifaList.as_view(), name='listar-tarifas'),
    
    
    path('tarifas/criar/', TarifaCreate.as_view(), name='criar-tarifa'),
    
    path('editar/<int:pk>/', views.TarifaUpdate.as_view(), name='editar-tarifa'),
    
   
    path('tarifas/<int:pk>/excluir/', TarifaDelete.as_view(), name='excluir-tarifa'),
]
