from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

url_base="http://127.0.0.1:8000/"
def cambiar_paso2(request):
    print('Verificando codigo')
    return render(request,'paginas/recuperarContrasena3.html')

def paso_2(request):
    return render(request,'paginas/recuperarContrasena2.html')

def cambiar_paso1(request):#Aqui va la revision de la cuenta y se envia el codigo, se redirecciona a la siguiente pagina
    print('Enviando email')
    print(request.session['correo'])
    #return redirect(request,'contra2')
    #return redirect(request,'login/recuperarEnvio')#no me redirecciona como es
    #return paso_2(request)
    #return redirect(request,'login/recuperar/codigo')
    return render(request,'paginas/recuperarContrasena2.html')

def paso_1(request):
    return render(request,'paginas/recuperarContrasena1.html')
