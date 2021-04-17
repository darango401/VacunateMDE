from django.contrib import admin
from .models import *

# Register your models here.

class VacunadoAdmin(admin.ModelAdmin):
    list_display=("nombres", "apellidos", "tipo_documento", "numero_documento", "fecha_vacunacion","correo_electronico")
    search_fields=("nombres", "apellidos", "numero_documento","correo_electronico")
    list_filter=("fecha_vacunacion","comuna_residencia",)
    # date_hierarchy="fecha_vacunacion"

admin.site.register(Vacunado, VacunadoAdmin)

admin.site.site_header = 'Vacúnate Medellín'
admin.site.site_title = 'Portal Vacúnate Medellín'
admin.site.index_title = 'Bienvenido al portal de Vacúnate Medellín'
