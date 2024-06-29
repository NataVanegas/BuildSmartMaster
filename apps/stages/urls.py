# apps/stages/urls.py
from django.urls import path
from .views import (
    StageListView,
    StageDetailView,
    StageCreateView,
    StageUpdateView,
    StageDeleteView
)

app_name = 'stages'

urlpatterns = [
    path('', StageListView.as_view(), name='stage_list'),
    path('<int:pk>/', StageDetailView.as_view(), name='stage_detail'),
    path('create/', StageCreateView.as_view(), name='stage_create'),
    path('<int:pk>/edit/', StageUpdateView.as_view(), name='stage_update'),
    path('<int:pk>/delete/', StageDeleteView.as_view(), name='stage_delete'),
]
