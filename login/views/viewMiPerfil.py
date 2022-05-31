from django.shortcuts import render
from ..services import Servicios
Servi=Servicios()

def verMiPerfil(request):
    carrito=request.session['carrito']
    #print(f"El carrito tiene: {request.session['carrito']}")
    correo=request.session["correo"]
    rol=request.session['rol']
    usuario=Servi.perfil(correo)
    tarjetas=Servi.get_tarjetas_usuario(correo)
    datos={'correo':correo,'rol':rol,'usuario':usuario[0],'tarjetas':tarjetas,'carrito':carrito}
    return render(request,'paginas/miPerfil.html',datos)