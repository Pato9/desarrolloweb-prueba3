"""prueba2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

""" 
    Dicceionario de rutas!
"""
from django.contrib import admin
from django.urls import path
from prueba2.views import Inicio
from prueba2.views import QuienesSomos
from prueba2.views import Contacto
from prueba2.views import Galeria
from prueba2.views import ModeloMedida
from prueba2.views import modeloMetraje
from gestion.views import listar_casas
from gestion.views import agregar_cliente
from gestion.views import busqueda_habitacion
from gestion.views import busqueda_precio
from gestion.views import busqueda_precio_menor
from gestion.views import busqueda_precio_igual
from gestion.views import lista_clientes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Inicio/',Inicio),
    path('QuienesSomos/',QuienesSomos),
    path('Galeria/',Galeria),
    path('Contacto/',Contacto),
    path('Modelos/Modelo-medida/',ModeloMedida),
    path('Modelos/Modelo-metraje/', modeloMetraje),
    path('Casas/Lista/',listar_casas),
    path('Clientes/agregar/',agregar_cliente),
    path('Casas/listado-habitaciones/',busqueda_habitacion),
    path('Casas/listado-precios/',busqueda_precio),
    path('Casas/listado-precios-bajos/',busqueda_precio_menor),
    path('Casas/listado-precios-igual/',busqueda_precio_igual),
    path('Admin/Cliente/Listado/',lista_clientes),    
]
