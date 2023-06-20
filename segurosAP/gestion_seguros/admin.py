from django.contrib import admin
from .models import Cliente, Poliza, Asegurado, Certificado

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Poliza)
admin.site.register(Asegurado)
admin.site.register(Certificado)