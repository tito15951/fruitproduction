from django.db import models

class Usuario(models.Model):
    correo=models.EmailField(null=False,primary_key=True)
    nombre=models.TextField(max_length=30,null=False)
    contrasenia=models.TextField(max_length=20,null=False)
    rol=models.TextField(max_length=20,null=False,default='usuario')
    fecha_nac=models.DateField(null=False)

    def __str__(self):
        return self.nombre+'-'+self.correo

class MetodoPago(models.Model):
    num_tarjeta=models.TextField(max_length=16,primary_key=True,null=False)
    codigo=models.TextField(max_length=3,null=False)
    fecha_venc=models.DateField(null=False)
    nombre=models.TextField(max_length=30,null=False)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    saldo=models.IntegerField(null=False,default=0)

    def __str__(self):
        return str(self.id_usuario.correo)+'-****'+str(self.num_tarjeta[-4:]+" $"+str(self.saldo))

class Producto(models.Model):
    id=models.BigAutoField(primary_key=True)
    duenio=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nombre=models.TextField(max_length=30,null=False)
    valor=models.IntegerField(null=False)
    estado=models.TextField(default='espera')
    valoracion=models.IntegerField(default=0)
    #imagen=models.TextField(null=True)
    imagen=models.ImageField(upload_to='imagenes/',null=True)
    descripcion=models.TextField(null=False,default="Sin descripcion")
    presentacion=models.TextField(default="Molido",null=False)
    sabor=models.TextField(default="Chocolate",null=False)
    tueste=models.TextField(default="Medio",null=False)
    beneficio=models.TextField(default="Natural",null=False)
    variedad=models.TextField(default="Borbón",null=False)
    cantidad=models.IntegerField(null=False,default=1)
    def __str__(self):
        return str(self.id)+'-'+self.nombre+'('+self.duenio.correo+')'+'-$'+str(self.valor)

class Compra(models.Model):
    id=models.BigAutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    metodo_pago=models.ForeignKey(MetodoPago,on_delete=models.CASCADE,null=True)
    total=models.IntegerField(null=False)
    
    def __str__(self):
        return str(self.id)+'-'+self.usuario.correo+'($'+str(self.total)+')'

class CompraProducto(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_compra=models.ForeignKey(Compra,on_delete=models.CASCADE)
    id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.IntegerField(null=False)