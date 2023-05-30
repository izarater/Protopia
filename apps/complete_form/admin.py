from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Registro de modelo de ejemplo
from .models import Contacto

class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto

class ContactoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['Nombre']
    list_display = ('Nombre','Telefono','Telefono','Barrio','Municipio','xCoor','yCoor','Descripcion',)
    resource_class = ContactoResource


admin.site.register(Contacto,ContactoAdmin)