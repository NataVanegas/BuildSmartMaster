from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('create-remodeling/', views.create_remodeling, name='create_remodeling'),
    path('work-types/', views.work_type_list, name='work_type_list'),
    path('work-types/<int:pk>/', views.work_type_detail, name='work_type_detail'),
    path('work-types/<int:pk>/edit/', views.work_type_edit, name='work_type_edit'),
    path('work-types/<int:pk>/delete/', views.work_type_delete, name='work_type_delete'),
]
