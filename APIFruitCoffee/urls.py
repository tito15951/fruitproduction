from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from APIFruitCoffee.views.viewUsuario import User
from APIFruitCoffee.views.viewProducto import Product
from APIFruitCoffee.views.viewmetodopago import Metodo_Pago
from APIFruitCoffee.views.viewCompras import Comprar

urlpatterns = [
    path('api/usuarios',csrf_exempt(User.as_view()),name='usuarios'),
    path('api/productos',csrf_exempt(Product.as_view()),name='producto'),
    path('api/metodopago',csrf_exempt(Metodo_Pago.as_view()),name='MetodoPago'),
    path('api/compras',csrf_exempt(Comprar.as_view()),name='compras')
]

