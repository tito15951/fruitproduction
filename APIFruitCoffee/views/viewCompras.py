from django.views import View
from django.http import JsonResponse
import json

from numpy import product
from ..models import Producto, Usuario, Compra, CompraProducto, MetodoPago

class Comprar(View):
    def post(self,request):
        if ('nueva_compra' in request.POST):#Falta hacer que descuente de la tarjeta
            if ('usuario' in request.POST and 'productos' in request.POST):
                
                comprador=Usuario.objects.filter(correo=request.POST['usuario']).first()
                total=0
                #print(productosJson)
                productos=request.POST['productos']
                print(f"{productos} {type(productos)}")
                return JsonResponse({'Resp':"Hasta aqui voy bien"},safe=False,status=200)
                productosJson=json.loads(productos)
                
                
                
                print(f"Soy la api, recibí: {productosJson}")
                for producto in productosJson:
                    total+=producto["acumulado"]*producto["cantidad"]
                compra=Compra.objects.create(usuario=comprador,
                    total=total)
                for producto in productosJson:
                    producBD=Producto.objects.filter(id=producto['producto_id']).first()
                    CompraProducto.objects.create(
                        id_compra=compra,
                        id_producto=producBD,
                        cantidad=producto['cantidad']
                    )
                return JsonResponse({'Resp':True},safe=False,status=200)
            else:
                return JsonResponse({'Resp':"No implementado"},safe=False,status=404)
           
