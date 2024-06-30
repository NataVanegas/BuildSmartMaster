# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkTypeForm, StageForm
from apps.constructionMaterial.forms import MaterialForm
from .models import WorkType
from apps.stages.models import Stage
from apps.constructionMaterial.models import Material
from django.http import JsonResponse

def create_remodeling(request):
    if request.method == 'POST':
        work_form = WorkTypeForm(request.POST)
        if work_form.is_valid():
            new_work_type = work_form.save(commit=False)
            new_work_type.save()

            # Save the selected stages
            stages = work_form.cleaned_data['stages']
            for stage in stages:
                new_work_type.stages.add(stage)

                # Update each stage with materials
                materials = request.POST.getlist(f'materials_{stage.id}')
                if materials:
                    stage.materials.set(materials)
                stage.save()

            return redirect('core:create_remodeling')
    else:
        work_form = WorkTypeForm()
    return render(request, 'core/create_remodeling.html', {'work_form': work_form, 'stage_form': StageForm()})

def stage_materials(request, stage_id):
    materials = Material.objects.filter(stage_id=stage_id)
    materials_data = [{'id': material.id, 'name': material.name} for material in materials]
    return JsonResponse(materials_data, safe=False)
def index(request):
    return render(request, 'core/home.html')
