from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gestion_clientes/', views.gestion_clientes, name='gestion_clientes'),
    path('gestion_polizas/', views.gestion_polizas, name='gestion_polizas'),
    path('gestion_asegurados/', views.gestion_asegurados, name='gestion_asegurados'),
    path('gestion_clientes/cartera_cliente/<int:cliente_id>', views.cartera_cliente, name='cartera_cliente'),
    path('gestion_clientes/detalle_cliente/<int:cliente_id>', views.detalle_cliente, name='detalle_cliente'),
    path('gestion_polizas/detalle_poliza/<int:poliza_id>', views.detalle_poliza, name='detalle_poliza'),
    path('gestion_asegurados/cartera_asegurados/<int:poliza_id>', views.cartera_asegurados, name='cartera_asegurados'),
    path('gestion_asegurados/detalle_asegurado/<int:asegurado_id>', views.detalle_asegurado, name='detalle_asegurado'),
    
]
