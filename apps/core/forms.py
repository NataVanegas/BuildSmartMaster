from django import forms
from apps.core.models import WorkType
from apps.stages.models import Stage
from apps.constructionMaterial.models import Material

class WorkTypeForm(forms.ModelForm):
    stages = forms.ModelMultipleChoiceField(
        queryset=Stage.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = WorkType
        fields = ['name', 'description', 'stage']

class StageForm(forms.ModelForm):
    materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Stage
        fields = ['name', 'description', 'materials']