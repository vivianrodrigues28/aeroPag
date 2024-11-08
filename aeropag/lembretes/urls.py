# lembretes/urls.py
from django.urls import path
from .views import LembreteCreate, LembreteUpdate, LembreteDelete, LembreteList

urlpatterns = [
    path('cadastrar/lembrete/', LembreteCreate.as_view(), name='cadastrar-lembrete'),
    path('editar/lembrete/<int:pk>/', LembreteUpdate.as_view(), name='editar-lembrete'),
    path('excluir/lembrete/<int:pk>/', LembreteDelete.as_view(), name='excluir-lembrete'),
    path('listar/lembretes/', LembreteList.as_view(), name='listar-lembretes'),
    
]
