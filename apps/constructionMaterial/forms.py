# apps/constructionMaterial/forms.py
from django import forms
from .models import Material, MaterialCategory

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description', 'category', 'unit_price', 'image']

class MaterialCategoryForm(forms.ModelForm):
    class Meta:
        model = MaterialCategory
        fields = ['name', 'description']
