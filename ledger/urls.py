from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/add_image/', views.add_recipe_image, name='add_recipe_image'),

]
