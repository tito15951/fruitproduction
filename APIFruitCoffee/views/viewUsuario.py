from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from ..models import Usuario

class User(View):
    def get(self,request):
        if('listar' in request.GET):
            users=Usuario.objects.all()
            return JsonResponse(list(users.values('correo','nombre')),safe=False,status=200)
        if ('listar_vendedores' in request.GET):
            vendedores=Usuario.objects.filter(rol='vendedor')
            return JsonResponse(list(vendedores.values('correo','nombre')),safe=False,status=200)
        if ('listar_usuarios' in request.GET):
            clientes=Usuario.objects.filter(rol='cliente')
            return JsonResponse(list(clientes.values('correo','nombre')),safe=False,status=200)
        if ('listar_catadores' in request.GET):
            clientes=Usuario.objects.filter(rol='catador')
            return JsonResponse(list(clientes.values('correo','nombre')),safe=False,status=200)

        if('correo' in request.GET):
            correoRequest=request.GET['correo']
            user=Usuario.objects.filter(correo=correoRequest)
            return JsonResponse(list(user.values('correo','contrasenia','nombre','rol','fecha_nac')),safe=False,status=200)

        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)

    def post(self,request):
        if('setVendedor' in request.POST):
            try:
                correo=request.POST['setVendedor']
                user=Usuario.objects.filter(correo=correo).update(rol='vendedor')
                return JsonResponse({'Resp':True},safe=False,status=200)
            except:
                return JsonResponse({'Resp':False},safe=False,status=200)
        if('setCatador' in request.POST):
            try:
                correo=request.POST['setCatador']
                user=Usuario.objects.filter(correo=correo).update(rol='catador')
                return JsonResponse({'Resp':True},safe=False,status=200)
            except:
                return JsonResponse({'Resp':False},safe=False,status=200)
        
        if('setCliente' in request.POST):
            try:
                correo=request.POST['setCliente']
                user=Usuario.objects.filter(correo=correo).update(rol='cliente')
                return JsonResponse({'Resp':True},safe=False,status=200)
            except:
                return JsonResponse({'Resp':False},safe=False,status=200)
        if('login' in request.POST):
            if(('correo' in request.POST) and ('contrasenia' in request.POST)):
                correoRequest=request.POST['correo']
                contraseniaRequest=request.POST['contrasenia']
                user=Usuario.objects.filter(correo=correoRequest, contrasenia=contraseniaRequest)
                if(user.count()>0):
                    return JsonResponse({'Resp':True,'Rol':user.first().rol},safe=False,status=200)
                else:
                    return JsonResponse({'Resp':False},safe=False,status=200)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)

                
        elif('create' in request.POST):
            if(('correo' in request.POST) and ('nombre' in request.POST) and ('contrasenia' in request.POST) and ('rol' in request.POST) and ('fecha_nac' in request.POST)):
                try:
                    correoRequest=request.POST['correo']
                    nombreRequest=request.POST['nombre']
                    contraseniaRequest=request.POST['contrasenia']
                    rolRequest=request.POST['rol']
                    fecha_nacRequest=request.POST['fecha_nac']
                    newUser=Usuario.objects.create(correo=correoRequest,nombre=nombreRequest,contrasenia=contraseniaRequest, rol=rolRequest,fecha_nac=fecha_nacRequest)
                    return JsonResponse({'Resp':True},safe=False,status=201)
                except:
                    return JsonResponse({'Resp':False},safe=False,status=202)
 
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
        
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)


