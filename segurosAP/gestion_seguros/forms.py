from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente, Poliza, Asegurado

TYPE_CHOICES={
    ("general", "General"),
    ("diploma_tramite", "Diploma en trámite"),
    ("otros", "Otros")
}

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class AltaClienteForm(ClienteForm):
    def clean(self):
        documento = self.cleaned_data["documento"]
        if Cliente.objects.filter(documento = documento).exists():
            raise ValidationError("Ya hay un cliente inscripto con ese documento")
        
        return self.cleaned_data
    
class ModificarClienteForm(ClienteForm):  
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        #self.fields['documento'].widget.attrs.update({"readonly": True, 'disabled': True})   
    
    def clean(self):
        documento = self.cleaned_data["documento"]
        if Cliente.objects.filter(documento = documento).exists():
            raise ValidationError("Ya hay un cliente inscripto con ese documento")
        
        return self.cleaned_data
    
  

class AltaPolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            ),
            "fecha_fin": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            ),
            "fecha_limite_carga": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            )
        }

    def clean(self):
        fecha_inicio = self.cleaned_data["fecha_inicio"]
        fecha_fin = self.cleaned_data["fecha_fin"]
        if fecha_inicio > fecha_fin:
            raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio")
        
        return self.cleaned_data
    
class ModificarPolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            ),
            "fecha_fin": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            ),
            "fecha_limite_carga": forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            )
        }

    def clean(self):
        fecha_inicio = self.cleaned_data["fecha_inicio"]
        fecha_fin = self.cleaned_data["fecha_fin"]
        if fecha_inicio > fecha_fin:
            raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio")
        
        return self.cleaned_data
    

class AseguradoForm(forms.ModelForm):
    class Meta:
        model = Asegurado
        fields = "__all__"

    def clean(self):
        poliza = self.cleaned_data["poliza"]
        poliza_=Poliza.objects.filter(id=poliza.id)[0]
        print(poliza_.asegurados)
        if len(poliza_.asegurados.all()) >= poliza_.limite_asegurados:
            raise ValidationError("Ya hay un asegurado inscripto con ese documento")
        
        return self.cleaned_data
    
class AltaAseguradoForm(AseguradoForm):

    pass
    

class ModificarAseguradoForm(AseguradoForm):
    class Meta:
        model = Asegurado
        fields = "__all__"
