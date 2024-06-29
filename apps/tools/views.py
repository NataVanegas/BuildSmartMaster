# apps/tools/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Tool, ToolCategory
from .forms import ToolForm, ToolCategoryForm

# Tool Views
def tool_list(request):
    tools = Tool.objects.all()
    return render(request, 'tools/tool_list.html', {'tools': tools})

def tool_detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    return render(request, 'tools/tool_detail.html', {'tool': tool})

def tool_create(request):
    if request.method == "POST":
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save()
            return redirect('tools:tool_detail', pk=tool.pk)
    else:
        form = ToolForm()
    return render(request, 'tools/tool_form.html', {'form': form})

def tool_update(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == "POST":
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            tool = form.save()
            return redirect('tools:tool_detail', pk=tool.pk)
    else:
        form = ToolForm(instance=tool)
    return render(request, 'tools/tool_form.html', {'form': form})

def tool_delete(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == "POST":
        tool.delete()
        return redirect('tools:tool_list')
    return render(request, 'tools/tool_confirm_delete.html', {'tool': tool})

# ToolCategory Views
def tool_category_list(request):
    categories = ToolCategory.objects.all()
    return render(request, 'tools/tool_category_list.html', {'categories': categories})

def tool_category_create(request):
    if request.method == 'POST':
        form = ToolCategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('tools:tool_category_detail', pk=category.pk)
    else:
        form = ToolCategoryForm()
    return render(request, 'tools/tool_category_form.html', {'form': form})

def tool_category_detail(request, pk):
    category = get_object_or_404(ToolCategory, pk=pk)
    return render(request, 'tools/tool_category_detail.html', {'category': category})

def tool_category_update(request, pk):
    category = get_object_or_404(ToolCategory, pk=pk)
    if request.method == "POST":
        form = ToolCategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('tools:tool_category_detail', pk=category.pk)
    else:
        form = ToolCategoryForm(instance=category)
    return render(request, 'tools/tool_category_form.html', {'form': form})

def tool_category_delete(request, pk):
    category = get_object_or_404(ToolCategory, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('tools:tool_category_list')
    return render(request, 'tools/tool_category_confirm_delete.html', {'category': category})

# Modal 
def save_tool_form(request, pk=None):
    if pk:
        tool = get_object_or_404(Tool, pk=pk)
    else:
        tool = Tool()
    
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES, instance=tool)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = ToolForm(instance=tool)
    
    context = {'form': form}
    html_form = render_to_string('tools/tool_form_modal.html', context, request=request)
    return JsonResponse({'html_form': html_form})


