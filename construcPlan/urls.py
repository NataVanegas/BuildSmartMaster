# proyectoConstrucPlan/urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('materials/', include('apps.constructionMaterial.urls')),
    path('tools/', include('apps.tools.urls')),
     path('stages/', include('apps.stages.urls', namespace='stages')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
