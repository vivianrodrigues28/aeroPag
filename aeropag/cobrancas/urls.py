from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cobrancas, name='listar_cobrancas'),
    path('nova/', views.criar_cobranca, name='criar_cobranca'),
    path('editar/<int:id>/', views.editar_cobranca, name='editar_cobranca'),
    path('excluir/<int:id>/', views.excluir_cobranca, name='excluir_cobranca'),
    path('<int:id>/', views.detalhes_cobranca, name='detalhes_cobranca'),
]
