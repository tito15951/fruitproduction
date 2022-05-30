from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def verMisProductos(request):
    print(request.session['correo'])
    correo=request.session['correo']
    rol=request.session['rol']
    resp=Servi.listar_productos_dueno(correo)
    datos={'correo':correo,
            'rol':rol,
            'productos':resp}
    #print(resp)
    return render(request,'paginas/misProductos.html',datos)

def eliminarProducto(request):
        id=request.POST.get('id')
        resp=Servi.eliminar_producto(id)
        if(resp['Resp']==True):
                print('eliminado correctamente')
                messages.info(request,'Producto eliminado exitosamente')                
        else:
                messages.error(request,'No se pudo eliminar el producto')
        return HttpResponseRedirect('misproductos')