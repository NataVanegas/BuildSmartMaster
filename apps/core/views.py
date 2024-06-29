from django.shortcuts import render, redirect
from .forms import WorkForm
from .models import WorkType

def create_remodeling(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            # Get the work type from the form's cleaned data
            work_type = form.cleaned_data['work_type']
            # Create a new WorkType object with the entered work type
            new_work_type = WorkType.objects.create(name=work_type)

            # Logic to save stages, materials, and tools (assuming they are ModelForms)
            # ... (your existing logic for saving stages, materials, and tools)

            return redirect('core:index')
        else:
            form = WorkForm()
    else:
        form = WorkForm()
    return render(request, 'core/create_remodeling.html', {'form': form})

def index(request):
    return render(request, 'core/index.html')
