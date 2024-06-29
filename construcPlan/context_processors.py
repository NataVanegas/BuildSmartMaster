# construcPlan/context_processors.py
from apps.stages.models import Stage

def stages_context(request):
    stages = Stage.objects.all()
    return {'stages': stages}
