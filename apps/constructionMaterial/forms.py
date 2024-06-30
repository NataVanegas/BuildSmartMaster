# apps/constructionMaterial/forms.py
from django import forms
from .models import Material, MaterialCategory

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description', 'image', 'category', 'unit_price',  'stock_quantity']

class MaterialCategoryForm(forms.ModelForm):
    class Meta:
        model = MaterialCategory
        fields = ['name', 'description']
