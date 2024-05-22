from Fomularios import ModuloGeneral as gen
from util import Ventana as util_ventana
import tkinter as tk
import pandas as pd

    

#FUNCIONES PARA AÑADIR CATEGORÍA
def añadirCategoria(categorías):  #Cuando se presiona el botón añadir categoría
    #Crear el popUp
    popUp = tk.Toplevel()
    popUp.geometry("300x150")
    popUp.resizable(0,0)
    popUp.title("Añadir una categoría")
    w,h = 300, 100
    util_ventana.centrarVentana(popUp,w,h)
    #Configurar las columnas y filas para el centrado
    popUp.columnconfigure(0, weight=1)
    popUp.columnconfigure(1, weight=1)
    popUp.columnconfigure(2, weight=1)
    popUp.columnconfigure(3, weight=1)
    popUp.rowconfigure(0, weight=1)
    popUp.rowconfigure(1, weight=1)
    popUp.rowconfigure(2, weight=1)
    popUp.rowconfigure(3, weight=1)
    #Labels con las instrucciones
    username_label = tk.Label(popUp, text = "Escriba el nombre de la categoría")
    username_label.grid(column=0, row=0, padx=5, pady=5, columnspan=4)
    #Colocar la caja de texto para que el usuario ingrese el nombre
    cajaTexto1 = tk.Entry(popUp)
    cajaTexto1.grid(column = 0, row = 1, padx=5, pady=5, columnspan=4, sticky=tk.EW)
    #Boton aceptar
    aceptar = tk.Button(popUp, text = "Aceptar", command = lambda: aceptarCategoria(popUp,cajaTexto1,categorías))
    aceptar.grid(column = 1, row=2, padx=5, pady=5, sticky=tk.E)
    #Boton Cancelar
    cancel = gen.cancelar(popUp)
    cancel.grid(column = 2, row=2, padx=5, pady=5, sticky=tk.W)
    
def aceptarCategoria(popUp,cajaTexto1,categorías): #Cuando se presiona el botón aceptar en el popup Añadir Categoría
    categoria = cajaTexto1.get() #Recuperar el texto de la caja y guardarlo en la variable categoría
    error = False #Variable para control de errores
    #Si la caja de texto está vacía, mostrar error
    if categoria == "":
        error = True
        gen.advertencia("Por favor ingrese un nombre para la categoría",cajaTexto1)
    if categoria in categorías.values:
            error = True
            gen.advertencia("Esta categoría ya ha sido registrada. Intente de nuevo",cajaTexto1)
    if error == False:
        categorías.loc[len(categorías)] = [categoria]
        categorías.to_csv("categorías.csv")
        print(categorías) #Print temporal para verificar que funciona el programa
        popUp.destroy() #Destruir el popup
    
#FUNCIONES PARA AÑADIR PRODUCTO
def añadirProducto(productos,categorías,Textocaja1 = "no",Textocaja2="no",command_cancel="destroy"):
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
    #Si el parámetro "cajas" es verdadero, poner texto de relleno en las cajas
    if Textocaja1 != "no":
        cajaTexto1.insert(0,Textocaja1)
    if Textocaja2 != "no":
        cajaTexto2.insert(0,Textocaja2)
    #Menu de categorías
    global categoria
    categoria = tk.StringVar(popUp,"Categoría")
    menu = tk.OptionMenu(popUp, categoria, *categorías["categorías"]) 
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
        if producto in productos.producto.values:
            error = True
            gen.advertencia("Ya existe un producto con este nombre", cajaTexto1)
        #Agregar el producto al diccionario de productos, con su precio
        if error == False:
            productos.loc[len(productos)] = [producto, precio, categoria]
            productos.to_csv("productos.csv")
            print(productos) #Print temporal para ver si funciona correctamente
            popUp.destroy()
            #Si el precio ingresado no es un número, mostrar error
    except TypeError:
        gen.advertencia("El precio ingresado no es válido. Por favor intente de nuevo", cajaTexto2)
        
#FUNCIONES DEL BUSCADOR
def texto_buscador_productos(evento,buscador_productos):
    buscador_productos.insert(0,"🔎                       Buscar un producto")

def buscar_producto(self,evento,buscador_productos,productos,ventana):
    find = False
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
                    find = True
        if find !=True:
            gen.advertencia("El producto no se ha encontrado")
    except KeyError:
        gen.advertencia("El producto no se ha encontrado")
        
def editar_producto(productos,x,y,ventana,nombreL,precioL,categoriaL,editar,eliminar,volver):
    editado = productos[x].pop(y)
    añadirProducto(productos,y,editado,command_cancel=lambda:cancel_Edit(productos,x,y,editado))
    regresar(nombreL,precioL,categoriaL,editar,eliminar,volver)
    
def cancel_Edit(productos,x,y,editado):
    productos[x][y] = editado
    print(productos)
    
def eliminar_producto(productos,x,y,nombreL,precioL,categoriaL,editar,eliminar,volver):
    productos[x].pop(y)
    print(productos)
    gen.advertencia("El producto ha sido eliminado")
    regresar(nombreL,precioL,categoriaL,editar,eliminar,volver)
        
def regresar(nombreL,precioL,categoriaL,editar,eliminar,volver):
    nombreL.destroy()
    precioL.destroy()
    categoriaL.destroy()
    editar.grid_forget()
    eliminar.grid_forget()
    volver.grid_forget()

