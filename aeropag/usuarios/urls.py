from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, recuperacao_view, login_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("cadastro/", UsuarioCreate.as_view(), name="cadastro"),
    # path('recuperacao/', recuperacao_view, name='recuperacao'),
    path("registrar/", UsuarioCreate.as_view(), name="registrar"),
    # path('recuperacao/', recuperacao_view, name='recuperacao'),
    # Recuperação de Senha
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password-reset-form.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password-reset-done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password-reset-confirm.html",
            success_url=reverse_lazy("login"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
