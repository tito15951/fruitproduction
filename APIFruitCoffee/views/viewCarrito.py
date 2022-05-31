# from itertools import product
#from ..models import Producto, Usuario


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        #print (self.session)
        carrito =self.session.get('carrito')
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def add_producto_carrito(self, producto):
        id = str(producto.id)
        #print(id)
        #print(self.carrito)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.valor,
                "cantidad": 1,
            }
            #print("lo repeti socio")

        else:
            for key,value in self.carrito.items():
                if key == id:
                    value["cantidad"]=value["cantidad"]+1
                    break
                
        self.save_carrito()

    def save_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def delete_producto_carrito(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.save_carrito()
    
    def rest_producto_cant(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            #print(id)
            self.carrito[id]["cantidad"] =  self.carrito[id]["cantidad"]-1
            self.carrito[id]["acumulado"] -= producto.valor
            if self.carrito[id]["cantidad"] < 1: 
                self.delete_producto_carrito(producto)
            self.save_carrito
    
    def clear_carrito(self):
        self.session["carrito"]={}
        self.session.modified = True


