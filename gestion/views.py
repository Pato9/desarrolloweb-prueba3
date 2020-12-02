from django.shortcuts import render
from django.http import HttpResponse
from gestion.models import Casa

# Create your views here.

def busqueda_casa(request):
    return render(request,"busqueda-casa.html")

def listar_casas():
    #TODO: LISTAR LAS CASAS ! 
    # LAS CASAS NO VAN A POSEER FOTOS SE DEBE AGREGAR LA OPCION DE INGRESAR CORREO PARA
    #SOLICITAR IMAGENES DE ELLAS.

