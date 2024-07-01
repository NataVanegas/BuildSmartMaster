# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkTypeForm, StageForm
from apps.constructionMaterial.forms import MaterialForm
from .models import WorkType
from apps.stages.models import Stage
from apps.core.models import WorkType
from apps.constructionMaterial.models import Material
from django.http import JsonResponse

def work_type_list(request):
    work_types = WorkType.objects.all()
    return render(request, 'core/work_type_list.html', {'work_types': work_types})

def work_type_detail(request, pk):
    work_type = get_object_or_404(WorkType, pk=pk)
    return render(request, 'core/work_type_detail.html', {'work_type': work_type})

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

            return redirect('core:index')
    else:
        work_form = WorkTypeForm()
    return render(request, 'core/create_remodeling.html', {'work_form': work_form, 'stage_form': StageForm()})

def work_type_edit(request, pk):
    work_type = get_object_or_404(WorkType, pk=pk)
    if request.method == "POST":
        form = WorkTypeForm(request.POST, instance=work_type)
        if form.is_valid():
            form.save()
            return redirect('core:work_type_detail', pk=work_type.pk)
    else:
        form = WorkTypeForm(instance=work_type)
    return render(request, 'core/work_type_edit.html', {'form': form, 'work_type': work_type})

def work_type_delete(request, pk):
    work_type = get_object_or_404(WorkType, pk=pk)
    if request.method == "POST":
        work_type.delete()
        return redirect('core:work_type_list')
    return render(request, 'core/work_type_confirm_delete.html', {'work_type': work_type})

def stage_materials(request, stage_id):
    materials = Material.objects.filter(stage_id=stage_id)
    materials_data = [{'id': material.id, 'name': material.name} for material in materials]
    return JsonResponse(materials_data, safe=False)

def home_view(request):
    work_types = WorkType.objects.all()
    stages = Stage.objects.all()  # Obtén las etapas asociadas si es necesario

    return render(request, 'core/home.html', {'work_types': work_types,'stages': stages})
def index(request):
    return render(request, 'core/home.html')
