# apps/stages/models.py
from django.db import models
from apps.constructionMaterial.models import Material
from apps.tools.models import Tool
from apps.core.models import WorkType

class Stage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    materials = models.ManyToManyField(Material)
    tools = models.ManyToManyField(Tool)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, related_name='stages')

    def __str__(self):
        return self.name
