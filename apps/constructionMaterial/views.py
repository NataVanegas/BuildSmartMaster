# apps/constructionMaterial/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Material, MaterialCategory
from .forms import MaterialForm, MaterialCategoryForm
from requests.exceptions import RequestException
from utils.serpapi import get_home_depot_product
import requests
from django.db.models import Q

# obtener productos de la API
API_KEY = "90c9ea2af52cdedc400ca2da9419b1540f3cde909659c234472160102e24f4ed"  # clave API

# Material Views

def material_list(request):
    """
    Vista para listar materiales y buscar materiales tanto localmente como a través de la API de Home Depot.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La página renderizada con la lista de materiales.
    """
    query = request.GET.get('query', '')
    materials = {}

    try:
        if query:
            # Filtrar materiales locales
            materials_local = Material.objects.filter(
                Q(name__icontains=query) |  # Filtrar por nombre
                Q(description__icontains=query)  # Filtrar por descripción
            )

            # Consultar API para obtener resultados adicionales
            api_data = get_home_depot_product(query, API_KEY)
            
            if isinstance(api_data, dict) and 'products' in api_data:
                api_data = api_data['products']
            elif not isinstance(api_data, list):
                api_data = []

            # Limitar a 10 resultados
            api_data = api_data[:10]
           
            materials_search = [
                {
                    'name': result.get('title', 'No Title'),
                    'unit_price': result.get('price', 'N/A'),
                    'image': result.get('thumbnails', 'No Image')
                }
                for result in api_data
            ]

            materials = {
                'materials_local': materials_local,
                'materials_search': materials_search
            }

        else:
            # Obtener todos los materiales locales si no hay consulta
            materials_local = Material.objects.all()
            
            materials = {
                'materials_local': materials_local,
                'materials_search': []  # Lista vacía si no hay consulta
            }
    except RequestException as e:
        # Manejo de errores
        print(f"Error fetching data from API: {e}")
        materials = {
            'materials_local': Material.objects.all(),
            'materials_search': []
        }

    return render(request, 'materials/material_list.html', materials)

def material_detail(request, pk):
    """
    Vista para mostrar el detalle de un material específico.

    Args:
        request: El objeto HttpRequest.
        pk: La clave primaria del material.

    Returns:
        HttpResponse: La página renderizada con los detalles del material.
    """
    material = get_object_or_404(Material, pk=pk)
    return render(request, 'materials/material_detail.html', {'material': material})

def material_create(request):
    """
    Vista para crear un nuevo material.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La página renderizada con el formulario de creación de material.
    """
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save()
            return redirect('materials:material_detail', pk=material.pk)
    else:
        form = MaterialForm()
    return render(request, 'materials/material_form.html', {'form': form})

def material_update(request, pk):
    """
    Vista para actualizar un material existente.

    Args:
        request: El objeto HttpRequest.
        pk: La clave primaria del material.

    Returns:
        HttpResponse: La página renderizada con el formulario de actualización de material.
    """
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            material = form.save()
            return redirect('materials:material_detail', pk=material.pk)
    else:
        form = MaterialForm(instance=material)
    return render(request, 'materials/material_form.html', {'form': form})

def material_delete(request, pk):
    """
    Vista para eliminar un material existente.

    Args:
        request: El objeto HttpRequest.
        pk: La clave primaria del material.

    Returns:
        HttpResponse: La página de confirmación de eliminación de material.
    """
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        material.delete()
        return redirect('materials:material_list')
    return render(request, 'materials/material_confirm_delete.html', {'material': material})

# MaterialCategory Views

def material_category_list(request):
    """
    Vista para listar todas las categorías de materiales.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La página renderizada con la lista de categorías de materiales.
    """
    categories = MaterialCategory.objects.all()
    return render(request, 'materials/material_category_list.html', {'categories': categories})

def material_category_create(request):
    """
    Vista para crear una nueva categoría de material.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La página renderizada con el formulario de creación de categoría de material.
    """
    if request.method == 'POST':
        form = MaterialCategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('materials:material_category_detail', pk=category.pk)
    else:
        form = MaterialCategoryForm()
    return render(request, 'materials/material_category_form.html', {'form': form})

def material_category_detail(request, pk):
    """
    Vista para mostrar el detalle de una categoría de material específica.

    Args:
        request: El objeto HttpRequest.
        pk: La clave primaria de la categoría de material.

    Returns:
        HttpResponse: La página renderizada con los detalles de la categoría de material.
    """
    category = get_object_or_404(MaterialCategory, pk=pk)
    return render(request, 'materials/material_category_detail.html', {'category': category})

def material_category_update(request, pk):
    """
    Vista para actualizar una categoría de material existente.

    Args:
        request: El objeto HttpRequest.
        pk: La clave primaria de la categoría de material.

    Returns:
        HttpResponse: La página renderizada con el formulario de actualización de categoría de material.
    """
    category = get_object_or_404(MaterialCategory, pk=pk)
    if request.method == "POST":
        form = MaterialCategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('materials:material_category_detail', pk=category.pk)
    else:
        form = MaterialCategoryForm(instance=category)
    return render(request, 'materials/material_category_form.html', {'form': form})

def material_category_delete(request, pk):
    """
    Vista para eliminar una categoría de material existente.

    Args:
        request: El objeto HttpRequest.
        pk: La clave primaria de la categoría de material.

    Returns:
        HttpResponse: La página de confirmación de eliminación de categoría de material.
    """
    category = get_object_or_404(MaterialCategory, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('materials:material_category_list')
    return render(request, 'materials/material_category_confirm_delete.html', {'category': category})

# Modal 

def save_material_form(request, pk=None):
    """
    Vista para manejar la lógica de guardado de materiales en un formulario modal.

    Args:
        request: El objeto HttpRequest.
        pk: La clave primaria del material (opcional).

    Returns:
        JsonResponse: JSON con el estado del formulario y el HTML del formulario modal.
    """
    data = dict()
    if pk:
        material = get_object_or_404(Material, pk=pk)
    else:
        material = Material()

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            # Return the updated list of materials or success message
        else:
            data['form_is_valid'] = False
    else:
        form = MaterialForm(instance=material)

    context = {'form': form}
    data['html_form'] = render_to_string('materials/material_form_modal.html', context, request=request)
    return JsonResponse(data)

def check_stock(request, material_id, material_search):
    """
    Vista para verificar el stock de un material utilizando la API de Home Depot.

    Args:
        request: El objeto HttpRequest.
        material_id: La clave primaria del material.
        material_search: El término de búsqueda del material.

    Returns:
        HttpResponse: La página renderizada con los resultados de la verificación de stock.
    """
    material = get_object_or_404(Material, id=material_id)
    if material:
        result = get_home_depot_product(material.name, API_KEY)
    else:
        result = get_home_depot_product(material_search, API_KEY)
    return render(request, 'materials/check_stock.html', {'material': material, 'result': result})
