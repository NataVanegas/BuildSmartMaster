from django import forms
from apps.core.models import WorkType
from apps.stages.models import Stage
from apps.constructionMaterial.models import Material
from apps.tools.models import Tool

class WorkTypeForm(forms.ModelForm):
    class Meta:
        model = WorkType
        fields = ['name', 'description']

class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['name', 'description']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description']

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'description']

class WorkForm(forms.Form):
    work_type = forms.CharField(label="Tipo de Trabajo", max_length=100)
    stages = forms.ModelMultipleChoiceField(queryset=Stage.objects.all(), widget=forms.CheckboxSelectMultiple, label="Etapas")
    materials = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), widget=forms.CheckboxSelectMultiple, label="Materiales")
    tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all(), widget=forms.CheckboxSelectMultiple, label="Herramientas")
