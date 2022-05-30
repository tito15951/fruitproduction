from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from numpy import True_
from ..services import Servicios
Servi=Servicios()

def registro(request):
    datos={'correo':'null'}
    return render(request,'paginas/registro.html',datos)

def registrarme(request):
    if(request.POST):
        if request.POST.get('nombre') and request.POST.get('email') and request.POST.get('reemail') and request.POST.get('contrasenia') and request.POST.get('recontrasenia'):
            correo=request.POST.get('email')
            confCorreo=request.POST.get('reemail')
            contra=request.POST.get('contrasenia')
            confContra=request.POST.get('recontrasenia')
            nombre=request.POST.get('nombre')
            if correo==confCorreo:
                pass
                if contra==confContra:
                    if len(contra)>7:
                        resp=Servi.registrarme(correo,contra,nombre,"cliente")
                        if resp['Resp']:
                            print('Redireccionando')
                            request.session['correo']=correo
                            request.session['rol']='cliente'
                            return redirect('index')

                        else:
                            messages.error(request,'El correo electrónico ya esta en uso')
                            return HttpResponseRedirect('registro')
                    else:
                        messages.error(request,'La contraseña debe de tener minimo 8 caracteres')
                        return HttpResponseRedirect('registro')
                else:
                    messages.error(request,'Las contraseñas no coinciden')
                    return HttpResponseRedirect('registro')
            else:
                messages.error(request,'Los correos no coinciden')
                return HttpResponseRedirect('registro')
        else:
            messages.error(request,'Por favor, ingrese todos los datos solicitados')
            return HttpResponseRedirect('registro')