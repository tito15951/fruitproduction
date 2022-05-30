from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib import sessions
from ..services import Servicios
Servi=Servicios()

def viewCatacion(request):
    correo=request.session['correo']
    rol=request.session['rol']
    pendientes=Servi.listar_producto_pendientes()
    datos={'correo':correo,'rol':rol,'pendientes':pendientes}
    #print(pendientes)
    return render(request,'paginas/panelCatacion.html',datos)