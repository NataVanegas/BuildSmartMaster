# apps/stages/forms.py
from django import forms
from .models import Stage
from apps.constructionMaterial.models import Material

class StageForm(forms.ModelForm):
    materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Stage
        fields = ['name', 'description', 'image', 'materials']
       
