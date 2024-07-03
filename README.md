# BuildSmartMaster
construcplan


Paso 1: Prerrequisitos
tener instalado 
-Python 3.8 o superior
-pip (gestor de paquetes de Python)
-MySQL (para la base de datos)


Paso 2: Crear y Activar un Entorno Virtual
Crea y activa un entorno virtual para aislar las dependencias del proyecto.

python -m venv myenv

# En Windows: 
myenv\Scripts\activate

Paso 3: Instalar Dependencias
Instala todas las dependencias necesarias desde el archivo requirements.txt.

pip install -r requirements.txt

Paso 4: Configurar la Base de Datos
Crear la base de datos en MySQL:

CREATE DATABASE buildsmartmaster CHARACTER SET UTF8;
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'contraseña';
GRANT ALL PRIVILEGES ON buildsmartmaster.* TO 'usuario'@'localhost';
FLUSH PRIVILEGES;

Configurar las credenciales de la base de datos:
En el archivo settings.py del proyecto, configura las credenciales de la base de datos:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'buildsmartmaster',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Paso 5: Aplicar Migraciones
Ejecuta las migraciones para crear las tablas en la base de datos.


python manage.py makemigrations
python manage.py migrate


Paso 6: Ejecutar el Servidor de Desarrollo
Inicia el servidor de desarrollo de Django.


python manage.py runserver

Abre tu navegador y ve a http://127.0.0.1:8000/ para ver el proyecto en acción.

Paso 9: Configuración para Generar PDFs
Instalar WeasyPrint:

pip install WeasyPrint
Configurar la generación de PDFs:
En tus vistas, utiliza WeasyPrint para generar PDFs. Por ejemplo:


from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_pdf(request, pk):
    work_type = get_object_or_404(WorkType, pk=pk)
    stages = work_type.stages.all()
    html_string = render_to_string('core/work_type_detail.html', {'work_type': work_type, 'stages': stages})
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="work_type_{pk}.pdf"'
    return response
Añadir la URL para la generación de PDFs:
python
Copiar código
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('work-type/<int:pk>/pdf/', views.generate_pdf, name='work_type_pdf'),
    # otras rutas...
]
Notas Adicionales
Static Files: Asegúrate de que tus archivos estáticos (CSS, JS, imágenes) están correctamente configurados en producción.
Security: Configura las variables de entorno para gestionar las credenciales y otros parámetros sensibles.
Testing: Realiza pruebas exhaustivas para asegurarte de que todo funciona como se espera.
Siguiendo estos pasos, deberías poder configurar y ejecutar tu proyecto Django con éxito. Si tienes alguna pregunta o problema, no dudes en pedirme ayuda.