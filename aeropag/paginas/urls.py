from django.urls import path
from .views import IndexView, DashboardView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
     path('dashboard/', DashboardView.as_view(), name='dashboard'),
     
]

