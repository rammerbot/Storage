from django import forms
from .models import Clients


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('code', 'name', 'last_name', 'phone')
        labels = {
            'code':'Codigo: ',
            'name': 'Nombre: ',
            'last_name':'Apellido: ',
            'phone':'Telefono: '
        }

class EditClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = 'name', 'last_name', 'phone'
        labels = {
            'name': 'Nombre: ',
            'last_name':'Apellido: ',
            'phone':'Telefono: '
        }
        widgets = {
            'name': forms.TextInput(attrs={ 'id':'edit_name'}),
            'last_name': forms.TextInput(attrs={'id':'edit_last_name'}),
            'phone': forms.TextInput(attrs={'id':'edit_phone'}),
        }