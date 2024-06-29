# apps/tools/urls.py
from django.urls import path
from . import views

app_name = 'tools'  # Este es el namespace

urlpatterns = [
    # Tool URLs
    path('', views.tool_list, name='tool_list'),
    path('<int:pk>/', views.tool_detail, name='tool_detail'),
    path('new/', views.tool_create, name='tool_create'),
    path('<int:pk>/edit/', views.tool_update, name='tool_update'),
    path('<int:pk>/delete/', views.tool_delete, name='tool_delete'),

    # Modal 
    path('modal/', views.save_tool_form, name='tool_form_modal'),
    path('modal/<int:pk>/', views.save_tool_form, name='tool_form_modal'),

    # ToolCategory URLs
    path('categories/', views.tool_category_list, name='tool_category_list'),
    path('categories/<int:pk>/', views.tool_category_detail, name='tool_category_detail'),
    path('categories/new/', views.tool_category_create, name='tool_category_create'),
    path('categories/<int:pk>/edit/', views.tool_category_update, name='tool_category_update'),
    path('categories/<int:pk>/delete/', views.tool_category_delete, name='tool_category_delete'),
]
