from django.db import models
from apps.stages.models import Stage
class WorkType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='work_types', blank=True)

    def __str__(self):
        return self.name
