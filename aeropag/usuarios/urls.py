from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, recuperacao_view 

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('recuperacao/', recuperacao_view, name='recuperacao'),  
]
