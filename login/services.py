import requests
class Servicios:
    def __init__(self):
        self.url_base="http://127.0.0.1:8000/"
        self.dir_usuarios="api/usuarios"
        self.dir_prodictos="api/productos"
        self.dir_tarjetas="api/metodopago"
        self.dir_pagos="api/compras"
    #              USUARIOS 
    
    def iniciarSesion(self,correo,contra):
        datos={
                'login':'',
                'correo':correo,
                'contrasenia':contra
            }
        url=self.url_base+self.dir_usuarios
        resp=requests.post(url,datos)
        respuestaJSON=resp.json()
        return respuestaJSON

    def registrarme(self,correo,contrasena,nombre,rol):
        datos={
            'create':'',
            'correo':correo,
            'nombre':nombre,
            'contrasenia':contrasena,
            'rol':rol,
            'fecha_nac':'2000-01-01'
        }
        url=self.url_base+self.dir_usuarios
        resp=requests.post(url,datos)
        return resp.json()
    
    def perfil(self,correo):
        url=self.url_base+self.dir_usuarios+"?correo="+correo
        resp=requests.get(url)
        return resp.json()

    def listar_vendedores(self):
        url=self.url_base+self.dir_usuarios+'?listar_vendedores'
        resp=requests.get(url)
        return resp.json()

    def listar_usuarios(self):
        url=self.url_base+self.dir_usuarios+'?listar_usuarios'
        resp=requests.get(url)
        return resp.json()

    def listar_catadores(self):
        url=self.url_base+self.dir_usuarios+'?listar_catadores'
        resp=requests.get(url)
        return resp.json()

    def ascender_usuario(self,correo):
        url=self.url_base+self.dir_usuarios
        datos={
            'setVendedor':correo
        }
        resp=requests.post(url,datos)
        return resp.json()

    def ascender_vendedor(self,correo):
        url=self.url_base+self.dir_usuarios
        datos={
            'setCatador':correo
        }
        resp=requests.post(url,datos)
        return resp.json()

    def desascender_catador(self,correo):
        url=self.url_base+self.dir_usuarios
        datos={
            'setCliente':correo
        }
        resp=requests.post(url,datos)
        return resp.json()

        #              PRODUCTOS

    def listar_productos(self):
        url=self.url_base+self.dir_prodictos+"?listar"
        resp=requests.get(url)
        return resp.json()

    def listar_productos_dueno(self,correo):
        url=self.url_base+self.dir_prodictos+'?BusquedaDuenio&duenio='+correo
        resp=requests.get(url)
        return resp.json()

    def buscar_producto_id(self,id):
        url=self.url_base+self.dir_prodictos+'?Busqueda&id='+id
        resp=requests.get(url)
        return resp.json()

    def filtrar_productos(self,filtro):
        url=self.url_base+self.dir_prodictos+'?filtrar'
        if 'nombre' in filtro:
            url+='&nombre='+str(filtro['nombre'])
            del filtro['nombre']
        if 'valoracion' in filtro:
            url+='&valoracion='+str(filtro['valoracion'])
            del filtro['valoracion']
        for llave, sabor in filtro.items():
            url+='&'+str(sabor)
        resp=requests.get(url)
        return resp.json()
        #print(f"La dirección final es: {url}")
    
    def listar_producto_pendientes(self):
        url=self.url_base+self.dir_prodictos+'?listarPendientes'
        resp=requests.get(url)
        return resp.json()
    
    def catar_producto(self,id,valoracion):
        url=self.url_base+self.dir_prodictos
        datos={'catar':id,'valoracion':valoracion}
        resp=requests.post(url,datos)
        return resp.json()

    def crear_producto(self,duenio,nombre,descripcion,presentacion,sabor,cantidad,valor,foto,tueste,beneficio,variedad):
        url=self.url_base+self.dir_prodictos
        print('Foto:',foto)
        datos={
            'create':'',
            'duenio': duenio,
            'nombre':nombre,
            'valor':valor,
            'imagen':foto,
            'descripcion':descripcion,
            'sabor':sabor,
            'presentacion':presentacion,
            'cantidad':cantidad,
            'tueste':tueste,
            'beneficio':beneficio,
            'variedad':variedad
        }
        resp=requests.post(url,datos)
        #return True
        return resp.json()

    def actualizar_producto(self,id,valor,descripcion,sabor, presentacion,cantidad,tueste,beneficio,variedad):
        url=self.url_base+self.dir_prodictos
        datos={'update':'',
                'id':id,
                'valor':valor,
                'descripcion':descripcion,
                'sabor':sabor,
                'presentacion':presentacion,
                'cantidad':cantidad,
                'tueste':tueste,
                'beneficio':beneficio,
                'variedad':variedad}
        resp=requests.post(url,datos)
        return resp.json()

    def eliminar_producto(self,id):
        url=self.url_base+self.dir_prodictos
        datos={
            'delete':'',
            'id':id
        }
        resp=requests.post(url,datos)
        return resp.json()

    #             TARJETAS
    def get_tarjetas_usuario(self,correo):
        url=self.url_base+self.dir_tarjetas+"?correo="+correo
        resp=requests.get(url)
        return resp.json()
    
    def new_tarjeta_usuario(self,correo,num_tarjeta,codigo,fecha_venc,nombre,saldo):
        url=self.url_base+self.dir_tarjetas
        datos={
            "create":"",
            "num_tarjeta":num_tarjeta,
            "codigo":codigo,
            "fecha_venc":fecha_venc,
            "nombre":nombre,
            "id_usuario":correo,
            "saldo":saldo
        }
        try:
            resp=requests.post(url,datos)
            return resp.json()
        except:
            print('Error interno')
            return {'Resp':False}
    
    def new_pago(self,usuario,productos):
        url=self.url_base+self.dir_pagos
        datos={
            "nueva_compra":"",
            "usuario":usuario,
            "productos":productos
        }
        print(f"Enviando {datos}")
        #print(f"Enviando: {usuario}({type(usuario)}) y {productos}({type(productos)})")
        resp=requests.post(url,datos)
        return resp.json()
        return True
    