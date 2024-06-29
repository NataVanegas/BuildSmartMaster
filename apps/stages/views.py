# apps/stages/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Stage
from .forms import StageForm

class StageListView(ListView):
    model = Stage
    template_name = 'stages/stage_list.html'
    context_object_name = 'stages'

class StageDetailView(DetailView):
    model = Stage
    template_name = 'stages/stage_detail.html'
    context_object_name = 'stage'

class StageCreateView(CreateView):
    model = Stage
    form_class = StageForm
    template_name = 'stages/stage_form.html'
    success_url = reverse_lazy('stages:stage_list')

class StageUpdateView(UpdateView):
    model = Stage
    form_class = StageForm
    template_name = 'stages/stage_form.html'
    success_url = reverse_lazy('stages:stage_list')

class StageDeleteView(DeleteView):
    model = Stage
    template_name = 'stages/stage_confirm_delete.html'
    success_url = reverse_lazy('stages:stage_list')

