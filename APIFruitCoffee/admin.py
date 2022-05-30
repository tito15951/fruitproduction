from django.contrib import admin

from APIFruitCoffee.models import Compra, CompraProducto, MetodoPago, Producto, Usuario


# Register your models here.
admin.site.register(Usuario)
admin.site.register(MetodoPago)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(CompraProducto)
