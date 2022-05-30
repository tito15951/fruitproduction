from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import sessions
from ..services import Servicios
Servi=Servicios()

def index(request):
    try:
        carrito=request.session['carrito']
    except:
        request.session['carrito']={}
        carrito=request.session['carrito']
    datos=0
    correo=0
    rol=0
    try:
        correo=request.session["correo"]
        rol=request.session['rol']
    except:
        correo='null'
        rol='null'
    resp={}#Servi.listar_productos()
    datos={'correo':correo,'productos':resp,'rol':rol,'carrito':carrito}
    #print(resp)
    return render(request,'paginas/index.html',datos)

def cerrarSesion(request):
    print('Eliminado sesion:',request.session['correo'])
    del request.session['correo']
    return HttpResponseRedirect('index')
    