from django.urls import path
from .views import TurmaCreate, AtividadeCreate, TurmaUpdate, AtividadeUpdate
from .views import TurmaDelete, AtividadeDelete
from .views import TurmaList, AtividadeList

urlpatterns = [
    path('cadastrar/turma/', TurmaCreate.as_view(), name='cadastrar-turma'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('editar/turma/&lt;int:pk&gt;/', TurmaUpdate.as_view(), name='editar-turma'),
    path('editar/atividade/&lt;int:pk&gt;/', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('excluir/turma/&lt;int:pk&gt;/', TurmaDelete.as_view(), name='excluir-turma'),
    path('excluir/atividade/&lt;int:pk&gt;/', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('listar/turmas/', TurmaList.as_view(), name='listar-turmas'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),

]