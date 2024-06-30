# apps/stages/models.py
from django.db import models
from apps.constructionMaterial.models import Material

class Stage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    materials = models.ManyToManyField(Material, related_name='stages', blank=True)

    def __str__(self):
        return self.name
