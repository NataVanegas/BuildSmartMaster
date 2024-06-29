# apps/constructionMaterial/forms.py
from django import forms
from .models import Tool, ToolCategory

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'description', 'category', 'unit_price', 'stock_quantity', 'image']

class ToolCategoryForm(forms.ModelForm):
    class Meta:
        model = ToolCategory
        fields = ['name', 'description']
