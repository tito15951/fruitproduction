from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import sessions
from django.contrib import messages

from ..models import Foto
from ..services import Servicios
Servi=Servicios()
def peticionCrearTarjeta(request):
    correo=request.session["correo"]
    numero_tarjeta=request.POST.get('num_tarjeta')
    cod_seguridad=request.POST.get('codigo')
    nombre=request.POST.get('nom_titular')
    anio=request.POST.get('anio')
    mes=request.POST.get('mes')
    saldo=request.POST.get('saldo')
    errores=0
    if (len(numero_tarjeta)<16 or len(numero_tarjeta)>16):
        errores+=1
        messages.error(request,'Porfavor ingrese una tarjeta valida')
    if (len(str(cod_seguridad))!=3):
        errores+=1
        messages.error(request,'Porfavor ingrese un codigo valido')
    if (len(nombre)<5):
        errores+=1
        messages.error(request,'Porfavor ingrese un nombre')
    if (anio=="null"):
        errores+=1
        messages.error(request,'Porfavor ingrese un año valido')
    if (mes=="null"):
        errores+=1
        messages.error(request,'Porfavor ingrese un mes valido')
    try:
        if (int(saldo)<=0):
            errores+=1
            messages.error(request,'Porfavor ingrese un saldo valido')
    except:
        errores+=1
        messages.error(request,'Porfavor ingrese un saldo valido')
    print('Los datos son:',f"{numero_tarjeta} {cod_seguridad} {nombre} {anio} {mes} {saldo}")
    if (errores==0):
        print('Guardando')
        resp=Servi.new_tarjeta_usuario(correo,numero_tarjeta,cod_seguridad,f"{anio}-{mes}-01",nombre,saldo)
        if(resp['Resp']):
            return redirect('perfil')
        else:
            messages.error(request,'Solo puede tener tres tarjetas activas')
            return HttpResponseRedirect('nuevoMetodo')
    else:
        return HttpResponseRedirect('nuevoMetodo')

def vistaNuevoMetodo(request):
    correo=request.session["correo"]
    rol=request.session['rol']
    anios=[]
    #meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    meses=[]
    for i in range(2022,2030):
        anios.append(i)
    for i in range(1,13):
        meses.append("0"+str(i) if i<=9 else str(i))
    #print(anios)
    #print(meses)
    datos={"anios":anios,"meses":meses,"correo":correo,"rol":rol}
    #print(datos)
    return render(request,"paginas/nuevoMetodo.html",datos)