from django.http import HttpResponse 
from django.template import Template, Context
#ejemplo de vista 


#Inicio vista
def Inicio(request):
    #Abrimos el documento que contiene la plantilla
    PlantillaInicio = open("prueba2/plantillas/index.html")
    #cargamos el documento en una variable de tipo 'Template'
    template = Template(PlantillaInicio.read())
    #Cerramos el documento externo 
    PlantillaInicio.close()
    #crear un contexto
    contexto = Context()
    #Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

#Quines somos vista
def QuienesSomos(request):
    plantillaQuines = open("prueba2/plantillas/Quienes-somos.html")
    template = Template(plantillaQuines.read())
    plantillaQuines.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

#Contacto vista
def Contacto(request):
    plantillaContacto = open("prueba2/plantillas/Contacto.html")
    template = Template(plantillaContacto.read())
    plantillaContacto.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

#Galeria vista
def Galeria(request):
    plantillaGaleria = open("prueba2/plantillas/Galeria.html")
    template = Template(plantillaGaleria.read())
    plantillaGaleria.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento) 

#Modelo medida vista
def ModeloMedida(request):
    plantillaModeloMedida = open("prueba2/plantillas/Modelo-medida.html")
    template = Template(plantillaModeloMedida.read())
    plantillaModeloMedida.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

#modelo metraje vista
def modeloMetraje(request):
    plantillaMetraje = open("prueba2/plantillas/modelo-metraje.html")
    template = Template(plantillaMetraje.read())
    plantillaMetraje.close()
    contexto = Context()
    documento =  template.render(contexto)
    return HttpResponse(documento)