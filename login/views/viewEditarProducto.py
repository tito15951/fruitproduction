from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import sessions
from django.contrib import messages

from login.FormProducto import FotoForm
from ..models import Foto
from ..services import Servicios
import shutil
Servi=Servicios()

def cargarEditarProducto(request):
    producto=0
    if(request.POST.get('id')):
        id=request.POST.get('id')
        request.session['editar']=True
        request.session['id_producto']=id
        print('enviado para editar',id)
        producto=Servi.buscar_producto_id(id)[0]
        #print(producto)
    else:
        request.session['editar']=False
        #print('enviado para crear')
    correo=request.session["correo"]
    rol=request.session['rol']
    tuestes=["Lijero","Medio","Oscuro"]
    beneficio=["Natural","Honey","Lavado"]
    variedad=["Castillo","Caturro","Borbón"]
    sabores=["Arándanos","Frambuesa","Piña","Coco","Avellana","Almendra","Nuez","Macadamia","Vainilla","Caramelo","Chocolate"]
    presentaciones=['Molido','En grano']
    sabores.sort()
    tuestes.sort()
    beneficio.sort()
    variedad.sort()
    presentaciones.sort()
    print(producto)
    datos={'correo':correo,'rol':rol,'presentaciones':presentaciones,'sabores':sabores,'producto':producto,'tuestes':tuestes,'beneficios':beneficio,'variedades':variedad}
    return render(request,'paginas/editarProducto.html',datos)

def guardarProducto(request):
    if(request.POST):
        foto=0
        form=FotoForm(request.POST, request.FILES)
        errores=0
        duenio=request.session['correo']
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        presentacion=request.POST.get('presentacion')
        sabor=request.POST.get('sabor')
        cantidad=request.POST.get('stock')
        valor=request.POST.get('valor')
        tueste=request.POST.get('tueste')
        beneficio=request.POST.get('beneficio')
        variedad=request.POST.get('variedad')

        
        #print('foto obtenida: ',foto)
        if(not form.is_valid() and request.session['editar'] == False):
            errores+=1
            messages.error(request,'Porfavor ingrese una imagen del producto')
        if(nombre==''):
            errores+=1
            messages.error(request,'Porfavor ingrese el nombre del producto')
        if(len(descripcion)<20):
            errores+=1
            messages.error(request,'Porfavor ingrese una descripción mas larga')
        if(presentacion=="0"):
            errores+=1
            messages.error(request,'Porfavor ingrese la presentación del producto')
        if(sabor=="0"):
            errores+=1
            messages.error(request,'Porfavor ingrese el sabor del producto')
        try:
            if (int(cantidad)<1):
                errores+=1
                messages.error(request,'Porfavor ingrese la cantidad de productos que tiene')
        except:
            errores+=1
            messages.error(request,'Porfavor ingrese la cantidad de productos que tiene')
        try:
            if(int(valor)<=0):
                errores+=1
                messages.error(request,'Porfavor ingrese el valor del producto')
        except:
            errores+=1
            messages.error(request,'Porfavor ingrese el valor del producto')
        if(tueste=='null'):
            errores+=1
            messages.error(request,'Porfavor ingrese el tueste del producto')
        if(beneficio=='null'):
            errores+=1
            messages.error(request,'Porfavor ingrese el beneficio del producto')
        if(variedad=='null'):
            errores+=1
            messages.error(request,'Porfavor ingrese la variedad del producto')
        #print('Datos a enviar:',valor,' ',descripcion,' ',sabor,' ',presentacion,' ',cantidad,' ',tueste,' ',beneficio,' ',variedad)
        if(errores==0):
            if(request.session['editar']==False):
                form.save()#Guadro la foto
                foto=Foto.objects.all().last()
                urlFoto=str(foto.foto)
                resp=Servi.crear_producto(duenio,nombre,descripcion,presentacion,sabor,cantidad,valor,urlFoto,tueste,beneficio,variedad)
                if(resp['Resp']==True):
                    messages.success(request,'Producto creado exitosamente')
                    return redirect('misproductos')
                else:
                    messages.error(request,'Hubo un problema al ingresar al producto, vuelve a intentarlo')
                    return HttpResponseRedirect('editarProducto')
            else:
                print('Guardando producto ya existente')
                del request.session['editar']
                tueste='Nada por ahora'
                beneficio='Nada por ahora'
                id=request.session['id_producto']
                resp=Servi.actualizar_producto(id,valor,descripcion,sabor,presentacion,cantidad,tueste,beneficio,variedad)
                messages.success(request,'Producto guardado exitosamente')
                return redirect('misproductos')
        else:
            return HttpResponseRedirect('editarProducto')
