from django.views import View
from django.http import JsonResponse
import json
from ..models import Producto, Usuario, Compra, CompraProducto, MetodoPago

class Comprar(View):
    def post(self,request):
        if ('nueva_compra' in request.POST):#Falta hacer que descuente de la tarjeta
            if ('usuario' in request.POST and 'productos' in request.POST and 'tarjeta' in request.POST):
                comprador=Usuario.objects.filter(correo=request.POST['usuario']).first()
                total=0
                #print(productosJson)
                productos=request.POST['productos']
                MetodoNormal=MetodoPago.objects.filter(num_tarjeta=request.POST['tarjeta'])
                Metodo=list(MetodoNormal.values())[0]
                
                print(f"{productos} {type(productos)}")
                productosJson=json.loads(productos)
            
                
                print(f"Soy la api, recibí: {productosJson}")
                for producto in productosJson:
                    total+=producto["acumulado"]*producto["cantidad"]
                if Metodo['saldo']>=total:
                    compra=Compra.objects.create(usuario=comprador,total=total,metodo_pago=MetodoNormal.first())
                    for producto in productosJson:
                        producBD=Producto.objects.filter(id=producto['producto_id']).first()
                        CompraProducto.objects.create(
                            id_compra=compra,
                            id_producto=producBD,
                            cantidad=producto['cantidad']
                        )
                    nuevoSaldo=Metodo['saldo']-total
                    Metodo=MetodoPago.objects.filter(num_tarjeta=request.POST['tarjeta']).update(saldo=nuevoSaldo)
                    return JsonResponse({'Resp':True},safe=False,status=200)
                else:
                    return JsonResponse({'Resp':False},safe=False,status=200)
                
            else:
                return JsonResponse({'Resp':"No implementado"},safe=False,status=404)
        else:
            print('esta mal la peticion')
            return JsonResponse({'Resp':"No implementado"},safe=False,status=404)
           
