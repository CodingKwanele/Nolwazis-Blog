from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('recipe/add/', views.recipe_create, name='recipe_create'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<slug:slug>/edit/', views.recipe_update, name='recipe_update'),
    path('recipe/<slug:slug>/delete/', views.recipe_delete, name='recipe_delete'),
    path('login/', LoginView.as_view(template_name='recipes/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
]
