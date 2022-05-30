from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def iniciarSesion(request):
    if(request.POST):
        if request.POST.get('email') and request.POST.get('contrasenia'):
            email=request.POST.get('email')
            contra=request.POST.get('contrasenia')
            respuestaJSON=Servi.iniciarSesion(email,contra)
            if respuestaJSON["Resp"]==True:
                request.session['correo']=email
                request.session['rol']=respuestaJSON['Rol']
                print(request.session['correo'])
                print(request.session['rol'])
                if (respuestaJSON['Rol']=='admin'):
                    return redirect('administracion')
                else:
                    return redirect('index')
            else:
                messages.error(request,'El usuario o la contraseña son incorrectos')
                return HttpResponseRedirect('login')
        else:
            messages.error(request,'Ingrese todos los datos')
            return HttpResponseRedirect('login')
    else:
        messages.error(request,'No implementado')
        return HttpResponseRedirect('login')
        
def inicio(request):
    carrito=request.session['carrito']
    datos={'correo':'null','carrito':carrito}
    return render(request,'paginas/iniciarSesion.html',datos)
    