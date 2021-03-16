"""
views.py : Contiene todas las vistas de nuestro proyecto Django

Django views for VacunateMedellin project.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/http/views/

"""

# Importamos el objeto HttpResponse
from django.http import HttpResponse
from django.template import Template, Context

# Creamos una vista en django declarando una función.
# Es decir, una función de estas representa una vista.
# Retorna la respuesta a la petición..
def inicio(request):

    doc_path = "VacunateMedellin/templates/index.html"
    doc_externo = open(doc_path, encoding='utf-8')

    # Creación del objeto de tipo Template
    tmp = Template(doc_externo.read())

    doc_externo.close()

    # Creación de contexto. Datos adicionales para el template.
    ctx = Context()

    # Renderizando el documento
    documento = tmp.render(ctx)

    return HttpResponse(documento)



def formulario(request):
    return HttpResponse("Esta será la página donde se ingresen los datos")

