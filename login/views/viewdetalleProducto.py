from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from login.services import Servicios
Servi=Servicios()

url_base="http://127.0.0.1:8000/"

def buscar_producto(request):
    if(request.POST):
        if request.POST.get('id'):
            correo=0
            rol=0
            try:
                correo=request.session["correo"]
                rol=request.session['rol']
            except:
                correo='null'
                rol='null'
            #print(request.POST.get('id'))
            id=request.POST.get('id')
            resp=Servi.buscar_producto_id(id)
            datos={"producto":resp[0],'correo':correo,'rol':rol}
            print(datos)
            return render(request, 'paginas/detalleProducto.html',datos)
        else:
            return HttpResponseRedirect('index')