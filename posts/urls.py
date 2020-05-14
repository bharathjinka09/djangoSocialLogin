from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.home),
    path('accounts/profile/post/<int:pk>/edit/', views.UpdatePostView.as_view()),
    path('accounts/profile/post/<int:id>/delete/', views.delete_post),
    path('not_logged_in', views.not_logged_in),
    path('create/', views.create),
    path('post/<int:id>/', views.post),
    path('post/<int:pk>/edit/', views.UpdatePostView.as_view(), name='update'),
    path('post/<int:id>/delete/', views.delete_post, name='delete-post'),
]
