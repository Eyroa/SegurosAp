from django.contrib import admin
from .models import Cliente, Poliza, Asegurado

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Poliza)
admin.site.register(Asegurado)
