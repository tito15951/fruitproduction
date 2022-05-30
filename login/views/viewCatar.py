from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from ..services import Servicios
Servi=Servicios()

def viewCatar(request):
    correo=request.session['correo']
    rol=request.session['rol']
    id=request.POST['id']
    producto=Servi.buscar_producto_id(id)
    datos={'correo':correo,
            'rol':rol,
            'producto':producto[0]}
    #print(datos)
    return render(request,'paginas/catarProducto.html',datos)

def CatarProducto(request):
    id=request.POST['id']
    valoracion=int(request.POST['valoracion'])
    if valoracion<=100 and valoracion >=0:
        Servi.catar_producto(id,valoracion)
        return redirect('catacion')
    else:
        return redirect('catacion')