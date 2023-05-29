from pyexpat import model
from .models import *
from django.forms import ModelForm, Form, ModelChoiceField,CheckboxSelectMultiple,ModelMultipleChoiceField
class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['Nombre', 'Telefono','Direccion','Barrio','Municipio','xCoor','yCoor','Descripcion','Oficios']
        widgets = {
            'Oficios':CheckboxSelectMultiple()
        }
        
class ContactoSelect(Form):
    def __init__(self,*args,**kwargs):
        self.user_id = kwargs.pop('user_id')
        super(ContactoSelect,self).__init__(*args,**kwargs)
        self.fields['ContactoSeleccionado'] = ModelChoiceField(queryset=Contacto.objects.filter(IdCreador=self.user_id),required=False,empty_label="Nuevo Contacto",label="Contacto a editar")

class OficioSelect(Form):
    ContactoSeleccionado = ModelChoiceField(queryset=None)
