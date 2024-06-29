# apps/constructionMaterial/urls.py
from django.urls import path
from . import views

app_name = 'materials'  # Este es el namespace

urlpatterns = [
    # Material URLs
    path('', views.material_list, name='material_list'),
    path('<int:pk>/', views.material_detail, name='material_detail'),
    path('new/', views.material_create, name='material_create'),
    path('<int:pk>/edit/', views.material_update, name='material_update'),
    path('<int:pk>/delete/', views.material_delete, name='material_delete'),

    # Modal URLs
    path('modal/', views.material_create, name='material_create'),
    path('modal/<int:pk>/', views.save_material_form, name='material_update'),
    
    # API externa URLs
    path('<int:material_id>/check_stock/', views.check_stock, name='check_stock'),

    # MaterialCategory URLs
    path('categories/', views.material_category_list, name='material_category_list'),
    path('categories/<int:pk>/', views.material_category_detail, name='material_category_detail'),
    path('categories/new/', views.material_category_create, name='material_category_create'),
    path('categories/<int:pk>/edit/', views.material_category_update, name='material_category_update'),
    path('categories/<int:pk>/delete/', views.material_category_delete, name='material_category_delete'),
]
