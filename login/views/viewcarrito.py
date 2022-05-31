import json
from django.contrib import messages
from django.shortcuts import render, redirect
from APIFruitCoffee.models import Producto
from APIFruitCoffee.views.viewCarrito import Carrito

from login.services import Servicios
Servi=Servicios()

def agregar_producto(request):
    id=request.POST.get('id')
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.add_producto_carrito(producto)
    return redirect('index')

def eliminar_producto(request):
    id=request.POST.get('id')
    carrito = Carrito(request)
    producto = Producto.objects.get(id)
    carrito.delete_producto_carrito(producto)
    return redirect('index')

def restar_producto(request):
    id=request.POST.get('id')
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.rest_producto_cant(producto)
    return redirect('index')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.clear_carrito()
    return redirect('index')

def comprar(request):
    #print('Comprando lo del carrito')
    carrito=request.session['carrito']
    usuario=request.session['correo']
    tarjeta=request.POST['tarjeta']
    lista=[]
    for key in carrito:
        lista.append(carrito[key])
    lista=json.dumps(lista)
    resp=Servi.new_pago(usuario,lista,tarjeta)
    print(resp)
    if resp['Resp']:
        messages.success(request,'La compra se ha realizado correctamente')
        request.session['carrito']={}
    else:
        messages.error(request,'No tiene suficiente saldo en la tarjeta')
    return redirect('index')