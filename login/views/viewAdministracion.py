from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib import sessions
import requests
from ..services import Servicios
Servi=Servicios()

def vistaAdmin(request):
    email=request.session['correo']
    rol=request.session['rol']
    vendedores=Servi.listar_vendedores()
    productos=Servi.listar_productos()
    usuarios=Servi.listar_usuarios()
    catadores=Servi.listar_catadores()
    print(productos)
    #print(catadores)
    datos={'correo':email,
        'rol':rol,
        'vendedores':vendedores,
        'productos':productos,
        'usuarios':usuarios,
        'catadores':catadores
    }
    return render(request,'paginas/vistaRoot.html',datos)

def ascenderUsuario(request):
    email=request.POST.get('correo')
    resp=Servi.ascender_usuario(email)
    return redirect('administracion')

def ascenderVendedor(request):
    email=request.POST.get('correo')
    resp=Servi.ascender_vendedor(email)
    return redirect('administracion')

def descenderCatador(request):
    email=request.POST.get('correo')
    resp=Servi.desascender_catador(email)
    return redirect('administracion')

def eliminarProducto(request):
        id=request.POST.get('id')
        resp=Servi.eliminar_producto(id)
        if(resp['Resp']==True):
                print('eliminado correctamente')
                messages.info(request,'Producto eliminado exitosamente')                
        else:
                messages.error(request,'No se pudo eliminar el producto')
        return HttpResponseRedirect('administracion')