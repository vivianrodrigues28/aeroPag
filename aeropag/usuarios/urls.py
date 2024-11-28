from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, recuperacao_view 

urlpatterns = [
     
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('cadastro/', UsuarioCreate.as_view(), name='cadastro'),
    path('recuperacao/', recuperacao_view, name='recuperacao'),  

    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('recuperacao/', recuperacao_view, name='recuperacao'),
    path('reset-password/', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='password_reset'),
         
    path('reset-password/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('reset/complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name='password_reset_complete'),  

]
