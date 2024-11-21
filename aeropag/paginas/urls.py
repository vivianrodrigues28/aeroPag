from django.urls import path
from .views import IndexView, DashboardView, search

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('search/', search, name='search'), 
]
