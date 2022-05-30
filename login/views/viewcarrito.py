import json
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
    print('Comprando lo del carrito')
    carrito=request.session['carrito']
    usuario=request.session['correo']
    lista=[]
    for key in carrito:
        lista.append(carrito[key])
    #print()
    #Servi.new_pago(usuario,json.loads(str(lista)))#Aca esta el error
    #Servi.new_pago(usuario,str(lista))
    return redirect('index')