# apps/stages/urls.py
from django.urls import path
from .views import (
    StageListView,
    StageDetailView,
    StageCreateView,
    StageUpdateView,
    StageDeleteView
)
from .views import generate_pdf

app_name = 'stages'

urlpatterns = [
    path('', StageListView.as_view(), name='stage_list'),
    path('<int:pk>/', StageDetailView.as_view(), name='stage_detail'),
    path('create/', StageCreateView.as_view(), name='stage_create'),
    path('<int:pk>/edit/', StageUpdateView.as_view(), name='stage_update'),
    path('<int:pk>/delete/', StageDeleteView.as_view(), name='stage_delete'),

  path('generate-pdf/<int:stage_id>/', generate_pdf, name='generate_pdf'),
]
