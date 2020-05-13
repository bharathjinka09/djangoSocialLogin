from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home),
    path('accounts/profile/', views.home),
    path('not_logged_in', views.not_logged_in),
]
