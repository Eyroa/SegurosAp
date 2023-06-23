from django.db import models

PROVINCIA_CHOICES = [
    ("BUE", "Buenos Aires"),
    ("SFE", "Santa Fe"),
    ("COR", "Córdoba"),
]

TIPO_PERSONA_CHOICES = [
    ("PF", "Persona Física"),
    ("PJ", "Persona Jurídica"),
]

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=64, verbose_name="Nombre o Razón Social")
    documento = models.CharField(max_length=16, verbose_name="CUIT/CUIL")
    email = models.EmailField(verbose_name="Email")
    domicilio_provincia = models.CharField(max_length=32, choices=PROVINCIA_CHOICES, verbose_name="Provincia")
    domicilio_ciudad= models.CharField(max_length=128, verbose_name="Ciudad")
    domicilio_calle= models.CharField(max_length=128, verbose_name="Calle")
    domicilio_numero= models.IntegerField(verbose_name="Número")
    domicilio_depto= models.CharField(max_length=128, verbose_name="Depto", null=True, blank=True)
    telefono = models.CharField(max_length=12, verbose_name="Teléfono", null=True)
    tipo_persona = models.CharField(max_length=16, choices=TIPO_PERSONA_CHOICES, verbose_name="Tipo de persona")

    def __str__(self):
        return self.nombre

class Poliza(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    numero = models.IntegerField(verbose_name="Número de póliza")
    tomador = models.CharField(max_length=128, verbose_name="Tomador")
    limite_asegurados = models.IntegerField(verbose_name="Límite de cantidad de asegurados")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio cobertura")
    fecha_fin = models.DateField(verbose_name="Fecha de fin cobertura")
    fecha_limite_carga = models.DateField(verbose_name="Fecha límite de actualización de nómina")
    condiciones = models.TextField(max_length=2048, verbose_name="Resumen condiciones de póliza")
    members = models.ManyToManyField(Cliente, related_name='polizas')
    
    def __str__(self):
        return self.numero

class Asegurado(models.Model):
    nombre = models.CharField(max_length=64, verbose_name="Nombre")
    apellido = models.CharField(max_length=64, verbose_name="Apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    documento = models.IntegerField(verbose_name="CUIT/CUIL")
    email=models.EmailField(verbose_name="Email")

class Certificado(models.Model):
    poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE)
    asegurado = models.ForeignKey(Asegurado, on_delete=models.CASCADE)
    numero = models.IntegerField(verbose_name="Número de certificado")
