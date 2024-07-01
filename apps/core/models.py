from django.db import models
from apps.stages.models import Stage

class WorkType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stages = models.ManyToManyField(Stage, related_name='work_types')

    def __str__(self):
        return self.name