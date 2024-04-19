#import ModuloGeneral as gen
from Fomularios import ModuloGeneral as gen
from util import Ventana as util_ventana
import tkinter as tk

#FUNCIONES PARA AÑADIR CATEGORÍA
def añadirCategoria(productos):  #Cuando se presiona el botón añadir categoría
    #Colocar el popUp
    popUp = tk.Toplevel()
    popUp.title("Añadir una categoría") #Título
    popUp.config(width=300, height=100) #Dimensiones
    util_ventana.centrarVentana(popUp, 300, 100)
    #Labels con las instrucciones
    tk.Label(popUp, text = "Escriba el nombre de la categoría").grid(row = 0, column = 0)
    #Colocar la caja de texto para que el usuario ingrese el nombre
    cajaTexto1 = tk.Entry(popUp)
    cajaTexto1.grid(row = 1, column = 1)
    #Botones aceptar y cancelar
    aceptar = tk.Button(popUp, text = "Aceptar", command = lambda: aceptarCategoria(popUp,cajaTexto1,productos))
    aceptar.grid(row = 2, column = 1)
    gen.cancelar(popUp, 2, 2)
    
def aceptarCategoria(popUp,cajaTexto1,productos): #Cuando se presiona el botón aceptar en el popup Añadir Categoría
    categoria = cajaTexto1.get() #Recuperar el texto de la caja y guardarlo en la variable categoría
    error = False #Variable para control de errores
    #Si la caja de texto está vacía, mostrar error
    if categoria == "":
        error = True
        gen.advertencia("Por favor ingrese un nombre para la categoría",cajaTexto1)
    for x in productos:
        if categoria == x:
            error = True
            gen.advertencia("Esta categoría ya ha sido registrada. Intente de nuevo",cajaTexto1)
    if error == False:
        productos[categoria] = {} #Añadir la variable categoría al diccionario productos como una key cuyo value es un diccionario vacío
        print(productos) #Print temporal para verificar que funciona el programa
        popUp.destroy() #Destruir el popup
    
#FUNCIONES PARA AÑADIR PRODUCTO
def añadirProducto(productos,command_cancel="destroy"):
    #Colocar el popUP
    popUp = tk.Toplevel()
    popUp.title("Añadir un producto") #Título
    w,h = 300, 100
    popUp.config(width=w, height=h) #Dimensiones
    util_ventana.centrarVentana(popUp,w,h)
    #Labels con las instrucciones
    tk.Label(popUp, text = "Nombre del producto").grid(row = 0, column = 1)
    tk.Label(popUp, text = "Precio del producto").grid(row = 0, column = 3)
    #Colocar cajas de texto para que el usuario ingrese los datos
    cajaTexto1 = tk.Entry(popUp)
    cajaTexto2 = tk.Entry(popUp)
    cajaTexto1.grid(row = 1, column = 1)
    cajaTexto2.grid(row = 1, column = 3)
    #Menu de categorías
    global categoria
    categoria = tk.StringVar(popUp,"Categoría")
    menu = tk.OptionMenu(popUp, categoria, *productos.keys()) 
    menu.grid(row=2, column = 1)
    #Botones aceptar y cancelar
    aceptar = tk.Button(popUp, text = "Aceptar", command = lambda: aceptarProducto(popUp,cajaTexto1,cajaTexto2,categoria,productos))
    aceptar.grid(row = 2, column = 2)
    gen.cancelar(popUp, 2, 3,command_cancel)
    
def aceptarProducto(popUp,cajaTexto1,cajaTexto2,categoria,productos):
    categoria = categoria.get()
    try:
        #Guardar el precio en una variable como un float con dos decimales
        precio = round(float(cajaTexto2.get()),2)
        #Recuperar el nombre del producto y guardarlo en una variable
        producto = cajaTexto1.get()
        error = False #Variable para control de errores
        #Si no se eligió una categoría, agregar por default a "Sin categoría":
        if categoria == "Categoría":
            categoria = "Sin categoría"
        #Si no se puso nombre al producto, mostrar error
        if producto == "":
            error = True
            gen.advertencia("Por favor poner nombre al producto",cajaTexto1)
        #Si el nombre del producto ya existe, mostrar error:
        for x in productos:
            for y in productos[x]:
                if producto == y:
                    error = True
                    gen.advertencia("Ya existe un producto con este nombre", cajaTexto1)
        #Agregar el producto al diccionario de productos, con su precio
        if error == False:
            productos[categoria][producto] = precio
            print(productos) #Print temporal para ver si funciona correctamente
            popUp.destroy()
            #Si el precio ingresado no es un número, mostrar error
    except:
        gen.advertencia("El precio ingresado no es válido. Por favor intente de nuevo", cajaTexto2)
        
#FUNCIONES DEL BUSCADOR
def texto_buscador_productos(evento,buscador_productos):
    buscador_productos.insert(0,"🔎                       Buscar un producto")

def buscar_producto(self,evento,buscador_productos,productos,ventana):
    busqueda = buscador_productos.get()
    buscador_productos.delete(0, tk.END)
    buscador_productos.insert(0,"🔎                       Buscar un producto")
    try:
        for x in productos:
            for y in productos[x]:
                if busqueda.lower() == y.lower():
                    nombreL = tk.Label(self, text = "Producto: "+ y)
                    nombreL.grid(row=4,column=2)
                    precioL = tk.Label(self, text = "Precio: Q." + str(productos[x][y]))
                    precioL.grid(row=5,column=2)
                    categoriaL = tk.Label(self, text = "Categoría: " + x)
                    categoriaL.grid(row=6,column=2)
                    editar = tk.Button(self,text="Editar",command=lambda:editar_producto(productos,x,y,ventana,nombreL,precioL,categoriaL,editar,eliminar,volver))
                    editar.grid(row=7,column=2)
                    eliminar=tk.Button(self, text="Eliminar",command=lambda:eliminar_producto(productos,x,y,nombreL,precioL,categoriaL,editar,eliminar,volver))
                    eliminar.grid(row=7,column=3)
                    volver= tk.Button(self, text="Volver",command=lambda:regresar(nombreL,precioL,categoriaL,editar,eliminar,volver))
                    volver.grid(row=7,column=1)
                else:
                    gen.advertencia("El producto no se ha encontrado")

    except KeyError:
        gen.advertencia("El producto no se ha encontrado")
def editar_producto(productos,x,y,ventana,nombreL,precioL,categoriaL,editar,eliminar,volver):
    productos[x]["editado"] = productos[x].pop(y)
    añadirProducto(productos,command_cancel=lambda:cancel_Edit(productos,x,y))
    productos[x].pop("editado")
    regresar(nombreL,precioL,categoriaL,editar,eliminar,volver)
    
def cancel_Edit(productos,x,y):
    productos[x][y] = productos[x].pop("editado")
    
def eliminar_producto(productos,x,y,nombreL,precioL,categoriaL,editar,eliminar,volver):
    productos[x].pop(y)
    gen.advertencia("El producto ha sido eliminado")
    regresar(nombreL,precioL,categoriaL,editar,eliminar,volver)
        
def regresar(nombreL,precioL,categoriaL,editar,eliminar,volver):
    nombreL.destroy()
    precioL.destroy()
    categoriaL.destroy()
    editar.grid_forget()
    eliminar.grid_forget()
    volver.grid_forget()
                    