from django.urls import path
from .views import viewInicioSesion
from .views import viewIndex
from .views import viewRegistro
from .views import viewContrasena
from .views import viewdetalleProducto
from .views import viewmisProductos
from .views import viewNuestrasRecetas
from .views import viewVerReceta
from .views import viewMiPerfil
from .views import viewBuscador
from .views import viewEditarProducto
from .views import viewAdministracion
from .views import viewMetodoPago
from .views import viewcarrito
from .views import viewCatacion
from .views import viewCatar
from APIFruitCoffee.views.viewStripe import (
    CreateCheckoutSessionView,
    ProductLandingPageView,
    SuccessView,
    CancelView,
    stripe_webhook,
    StripeIntentView)

urlpatterns =[
    #Retornan vistas
    path('',viewIndex.index,name='inicio'),
    path('login',viewInicioSesion.inicio,name='login'),
    path('index',viewIndex.index,name='index'),
    path('registro',viewRegistro.registro,name='registro'),
    path('login/recuperar1',viewContrasena.paso_1,name='contra1'),
    path('verProducto',viewdetalleProducto.buscar_producto,name='verProducto'),
    path('catacion',viewCatacion.viewCatacion,name='catacion'),
    path('catarProducto',viewCatar.viewCatar,name='catarProducto'),
    path('buscar',viewBuscador.buscador,name='buscar'),
    path('login/recuperar2',viewContrasena.paso_2,name='contra2'),
    path('misproductos',viewmisProductos.verMisProductos,name='misproductos'),
    path('nuestrasRecetas',viewNuestrasRecetas.verRecetas,name='nuestrasRecetas'),
    path('verReceta',viewVerReceta.verReceta,name='verReceta'),
    path('perfil',viewMiPerfil.verMiPerfil,name='perfil'),
    path('close',viewIndex.cerrarSesion,name='close'),
    path('editarProducto',viewEditarProducto.cargarEditarProducto,name='editarProducto'),
    path('administracion',viewAdministracion.vistaAdmin,name='administracion'),
    path('nuevoMetodo',viewMetodoPago.vistaNuevoMetodo,name='nuevoMetodo'),

        #Gestor Carrito
    path('Add', viewcarrito.agregar_producto, name="Add"),
    path('Del', viewcarrito.eliminar_producto, name="Del"),
    path('Sub', viewcarrito.restar_producto, name="Sub"),
    path('CLS', viewcarrito.limpiar_carrito, name="CLS"),
    path('comprarCarrito',viewcarrito.comprar,name='comprarCarrito'),
    #Hacer las peticiones
    path('iniciarSesion',viewInicioSesion.iniciarSesion,name='iniciarSesion'),
    path('registrarUsuario',viewRegistro.registrarme,name='registrarUsuario'),
    path('login/cambiarContrasena',viewContrasena.cambiar_paso1,name='cambiarContrasena1'),
    path('login/cambiarContrasena2',viewContrasena.cambiar_paso2,name='cambiarContrasena2'),
    path('guardarProducto',viewEditarProducto.guardarProducto,name='guardarProducto'),
    path('eliminarProducto',viewmisProductos.eliminarProducto,name='eliminarProducto'),
    path('eliminarProductoAdmin',viewAdministracion.eliminarProducto,name='eliminarProductoAdmin'),
    path('ascenderCliente',viewAdministracion.ascenderUsuario,name='ascenderCliente'),
    path('ascenderVendedor',viewAdministracion.ascenderVendedor,name='ascenderVendedor'),
    path('desascenderCatador',viewAdministracion.descenderCatador,name='desascenderCatador'),
    path('crearTarjeta',viewMetodoPago.peticionCrearTarjeta,name='crearTarjeta'),
    path('catacionProducto',viewCatar.CatarProducto,name='catacionProducto'),
    path('buscarProductos',viewBuscador.buscar,name='buscarProductos'),
    #Gestor Pagos
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')

]
