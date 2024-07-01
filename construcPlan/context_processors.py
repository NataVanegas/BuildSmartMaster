# construcPlan/context_processors.py
from apps.stages.models import Stage
from apps.core.models import WorkType
from apps.constructionMaterial.models import MaterialCategory

def stages_context(request):
    stages = Stage.objects.all()
    work_types = WorkType.objects.all()
    categories = MaterialCategory.objects.all()
    reponse={
        'stages': stages, 
        'work_types':work_types,
        'categories':categories
    }
    return reponse
