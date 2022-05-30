from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
#from sqlalchemy import delete
from ..models import Producto, Usuario

class Product(View):
    def get(self,request):
        if('listar' in request.GET):
            products=Producto.objects.all().exclude(estado='espera').order_by('-valoracion')
            return JsonResponse(list(products.values()),safe=False,status=200)
        elif('Busqueda' in request.GET):
            if('id' in request.GET):
                idRequest=request.GET['id']
                producto=Producto.objects.filter(id=idRequest)
                return JsonResponse(list(producto.values()),safe=False,status=200)
        elif('BusquedaDuenio' in request.GET):
            if('duenio' in request.GET):
                duenioRequest=request.GET['duenio']
                producto=Producto.objects.filter(duenio=duenioRequest)
                return JsonResponse(list(producto.values()),safe=False,status=200)
        elif('listarPendientes' in request.GET):
            productos=Producto.objects.all().exclude(estado='catado')
            return JsonResponse(list(productos.values()),safe=False,status=200)
        elif('filtrar' in request.GET):
            filtros={}
            productos=Producto.objects.all()
            if 'nombre' in request.GET:
                filtros['nombre']=request.GET['nombre']
            if 'valoracion' in request.GET:
                filtros['valoracion']=request.GET['valoracion']
            sabores=[]
            for item in request.GET:
                if item!='filtrar' and item!='nombre' and item !='valoracion':
                    sabores.append(item)
            if 'nombre' in request.GET:
                productos=Producto.objects.filter(
                    Q(valoracion__gte=int(filtros['valoracion'])) | Q(nombre__contains=filtros['nombre']) |
                    Q(sabor__in=sabores)
                    ).exclude(estado='espera').order_by('-valoracion')
            else:
                productos=Producto.objects.filter(
                    Q(valoracion__gte=int(filtros['valoracion'])) |
                    Q(sabor__in=sabores)
                    ).exclude(estado='espera').order_by('-valoracion')
            return JsonResponse(list(productos.values()),safe=False,status=200)
        else: 
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)
        

    def post(self,request):             
        if('create' in request.POST):
            if(('duenio' in request.POST) and ('nombre' in request.POST) and ('valor' in request.POST)):
                duenioRequest=request.POST['duenio']
                duenio1=Usuario.objects.filter(correo=duenioRequest).first()
                nombreRequest=request.POST['nombre']
                valorRequest=request.POST['valor']
                descripcionRequest=request.POST['descripcion']
                presentacionRequest=request.POST['presentacion']
                saborRequest=request.POST['sabor']
                tuesteRequest=request.POST['tueste']
                beneficioRequest=request.POST['beneficio']
                fotoRequest=request.POST['imagen']
                variedadRequest=request.POST['variedad']
                Producto.objects.create(duenio=duenio1,
                    nombre=nombreRequest, 
                    valor=valorRequest,
                    descripcion=descripcionRequest,
                    presentacion=presentacionRequest,
                    imagen=fotoRequest,
                    sabor=saborRequest,
                    tueste=tuesteRequest,
                    beneficio=beneficioRequest,
                    variedad=variedadRequest)
                return JsonResponse({'Resp':True},safe=False,status=201)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
        elif('delete' in request.POST):
            if(('id' in request.POST)):
                idRequest=request.POST['id']
                Producto.objects.filter(id=idRequest).delete()
                return JsonResponse({'Resp':True},safe=False,status=201)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
        elif('catar' in request.POST):
            if('valoracion' in request.POST):
                id=request.POST['catar']
                valoracion=request.POST['valoracion']
                Producto.objects.filter(id=id).update(valoracion=valoracion,estado='catado')
                return JsonResponse({'Resp':True},safe=False,status=200)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)

        elif('update' in request.POST):
            if(('id' in request.POST)):
                idRequest=request.POST['id']
                valorRequest=request.POST['valor']
                descripcionRequest=request.POST['descripcion']
                saborRequest=request.POST['sabor']
                presentacionRequest=request.POST['presentacion']
                cantidadRequest=request.POST['cantidad']
                tuesteRequest=request.POST['tueste']
                beneficioRequest=request.POST['beneficio']
                updateProduct=Producto.objects.filter(id=idRequest
                    ).update(valor=valorRequest,
                            descripcion=descripcionRequest,
                            presentacion=presentacionRequest,
                            sabor=saborRequest,
                            tueste=tuesteRequest,
                            beneficio=beneficioRequest,
                            cantidad=cantidadRequest)
                return JsonResponse({'Resp':True},safe=False,status=201)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)
