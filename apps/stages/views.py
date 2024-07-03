# apps/stages/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Stage
from .forms import StageForm
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from apps.constructionMaterial.models import Material

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


def generate_pdf(request, stage_id):
    stage = get_object_or_404(Stage, id=stage_id)
    materials = stage.materials.all()  # Assuming you have a related_name for materials in your Stage model
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="stage_{stage_id}.pdf"'

    buffer = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Get a sample stylesheet
    styles = getSampleStyleSheet()

    # Add stage details
    elements.append(Paragraph(f"Material List {stage.name}", styles['Title']))
    elements.append(Paragraph(f"{stage.description}", styles['BodyText']))
    elements.append(Paragraph("\n", styles['BodyText']))

    # Table header
    data = [['Material', 'Quantity', 'Price', 'Total']]

    # Table rows
    for material in materials:
        print(material)
        total = material.stock_quantity * material.unit_price
        print(total)
        data.append([material.name, material.stock_quantity, material.unit_price, total])

    # Create table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    buffer.build(elements)
    
    return response