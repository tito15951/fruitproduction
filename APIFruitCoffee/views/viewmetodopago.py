from telnetlib import STATUS
from django.views import View
from django.http import JsonResponse
from ..models import MetodoPago, Usuario


class Metodo_Pago(View):
    def get(self,request):
        if('listar' in request.GET):
            Pago=MetodoPago.objects.all()
            return JsonResponse(list(Pago.values('num_tarjeta','codigo','fecha_venc','nombre','id_usuario')),safe=False,status=200)
        elif('num_tarjeta' in request.GET):
            if('id' in request.GET):
                idRequest=request.GET['num_tarjeta']
                tarjeta=MetodoPago.objects.filter(num_tarjeta=idRequest).first()
                return JsonResponse(list(tarjeta.values()),safe=False,status=200)
        elif('correo' in request.GET):
            correo=request.GET['correo']
            tarjetas=MetodoPago.objects.filter(id_usuario=correo)
            return JsonResponse(list(tarjetas.values()),safe=False,status=200)
        else: 
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)

        

    def post(self,request):               
        if('create' in request.POST):
            if(('num_tarjeta' in request.POST) and 
                ('codigo' in request.POST) and 
                ('fecha_venc' in request.POST) and 
                ('nombre' in request.POST) and 
                ('id_usuario'in request.POST) and
                ('saldo' in request.POST)):
                print('Creando tarjeta')
                num_tarjetaRequest=request.POST['num_tarjeta']
                codigoRequest=request.POST['codigo']
                FechaVenRequest=request.POST['fecha_venc']
                nombreRequest=request.POST['nombre']
                idRequest=request.POST['id_usuario']
                saldoRequest=request.POST['saldo']
                usuario=Usuario.objects.filter(correo=idRequest).first()
                print(usuario)
                cantidadTarjetas=MetodoPago.objects.filter(id_usuario=idRequest).count()
                if cantidadTarjetas<=2:
                    MetodoPago.objects.create(num_tarjeta=num_tarjetaRequest,
                                        saldo=saldoRequest,codigo=codigoRequest, 
                                        fecha_venc=FechaVenRequest,
                                        nombre=nombreRequest,
                                        id_usuario=usuario)
                    print('Tarjeta creada')
                    return JsonResponse({'Resp':True},safe=False,status=200)
                else:
                    return JsonResponse({'Resp':False},safe=False,status=200)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
        
    
    
        elif('delete' in request.POST):
            if(('num_tarjeta' in request.POST)):
                idRequest=request.POST['id_usuario']
                MetodoPago.objects.filter(id=idRequest).delete()
                return JsonResponse({'Resp':True},safe=False,status=201)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)

