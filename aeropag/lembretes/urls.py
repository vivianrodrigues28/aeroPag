# lembretes/urls.py
from django.urls import path
from . import views  # Importando o módulo views
from .views import LembreteCreate, LembreteUpdate, LembreteDelete, LembreteList, excluir_lembrete

urlpatterns = [
    path('cadastrar/lembrete/', LembreteCreate.as_view(), name='cadastrar-lembrete'),
    path('editar/lembrete/<int:pk>/', LembreteUpdate.as_view(), name='editar-lembrete'),
    path('excluir/lembrete/<int:pk>/', LembreteDelete.as_view(), name='excluir-lembrete'),
    path('listar/lembretes/', LembreteList.as_view(), name='listar-lembretes'),
    path('excluir-lembrete/<int:id>/', excluir_lembrete, name='excluir-lembrete'),
    path('editar-lembrete/<int:id>/', views.editar_lembrete, name='editar-lembrete'),  # Correção
]
