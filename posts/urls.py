from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home),
    path('accounts/profile/', views.home),
    path('not_logged_in', views.not_logged_in),
    path('create/', views.create),
    path('post/<int:id>/', views.post),
    path('post/<int:id>/delete/', views.delete_post, name='delete-post'),
]
