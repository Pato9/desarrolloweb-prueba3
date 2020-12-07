from django.shortcuts import render
from django.http import HttpResponse
from gestion.models import Casa
from gestion.models import Cliente

# Create your views here.

def busqueda_casa(request):
    return render(request,"busqueda-casa.html")

def listar_casas(request):
    #TODO: LISTAR LAS CASAS ! 
    # LAS CASAS NO VAN A POSEER FOTOS SE DEBE AGREGAR LA OPCION DE INGRESAR CORREO PARA
    #SOLICITAR IMAGENES DE ELLAS.
    casas = Casa.objects.all()
    return render(request,'Lista-casas.html',{"casa": casas})
    #metodo que busca el precio exacto que se busco
def busqueda_precio_igual(request):
    if request.GET["precios"]:
        precios=request.GET["precios"]
        casas=Casa.objects.filter(precio=precios)
        return render(request,"lista_precios_igual.html",{"casa": casas})

    #metodo que busca si el precio es igual o menor
def busqueda_precio_menor(request):
    if request.GET["precios"]:
        precios=request.GET["precios"]
        casas=Casa.objects.filter(precio__lte=precios)
        return render(request,"lista_precios_bajo.html",{"casa": casas})

    #metodo que busca si el precio es igual o mayor
def busqueda_precio(request):
    if request.GET["precios"]:
        precios=request.GET["precios"]
        casas=Casa.objects.filter(precio__gte=precios)
        return render(request,"lista_precios.html",{"casa": casas})
    

def busqueda_habitacion(request):
    if request.GET["habitacion"]:
        habitacion=request.GET["habitacion"]
        casas = Casa.objects.filter(habitaciones=habitacion)
        return render(request,"lista_habitacion.html",{"casa": casas})


def agregar_cliente(request):
    #tomar los datos
    nombre = request.GET["nombre"]
    correo = request.GET["correo"]
    telefono = request.GET["telefono"]
    direccion = request.GET["direccion"]
    social = request.GET["social"]
    mensaje = request.GET["mensaje"]

    cli= Cliente(nombre = nombre,correo = correo,telefono=telefono,direccion=direccion,red_social=social,mensaje = mensaje)
    cli.save()
        
    return render(request,'agregar_cliente.html')
    
