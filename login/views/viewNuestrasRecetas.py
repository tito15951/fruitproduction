from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def verRecetas(request):
    correo=0
    rol=0
    try:
        correo=request.session["correo"]
        rol=request.session['rol']
    except:
        correo='null'
        rol='null'
    datos={'correo':correo,'rol':rol}
    return render(request,'paginas/nuestrasRecetas.html',datos)