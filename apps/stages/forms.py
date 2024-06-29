# apps/stages/forms.py
from django import forms
from .models import Stage

class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['name', 'description', 'materials', 'tools', 'work_type']
        widgets = {
            'materials': forms.CheckboxSelectMultiple,
            'tools': forms.CheckboxSelectMultiple,
        }
