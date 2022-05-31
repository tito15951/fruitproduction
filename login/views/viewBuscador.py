from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import sessions
import requests
from ..services import Servicios
Servi=Servicios()
sabores={
    "1":"Almendra",
    "2":"Arándanos",
    "3":"Avellana",
    "4":"Caramelo",
    "5":"Chocolate",
    "6":"Coco",
    "7":"Frambuesa",
    "8":"Macadamia",
    "9":"Nuez",
    "10":"Piña",
    "11":"Vainilla"
}
def buscar(request):
    
    filtro={}
    nombre=request.POST['nombre']
    if nombre!='':
        filtro['nombre']=nombre
    valoracion=int(request.POST['valoracion'])
    filtro['valoracion']=valoracion
    for key,sabor in sabores.items():
        if(sabor in request.POST):
            filtro[sabor]=sabor
    request.session['filtros']=filtro
    return redirect('buscar')

def buscador(request):
    correo=0
    rol=0
    carrito=request.session['carrito']
    try:
        filtros=request.session['filtros']
        #print(f"Los filtros para esta busqueda son: {filtros}")
        Productos=Servi.filtrar_productos(filtros)
        del request.session['filtros']
    except:
        Productos=Servi.listar_productos()
    try:
        correo=request.session["correo"]
        rol=request.session['rol']
    except:
        correo='null'
        rol='null'
    
    datos={'productos':Productos,'sabores':sabores,'correo':correo,'rol':rol,'carrito':carrito}
    return render(request,'paginas/buscador.html',datos)