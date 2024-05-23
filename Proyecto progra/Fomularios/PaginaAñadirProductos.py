import tkinter as tk
from Config import COLOR_CUERPO_PRINCIPAL
from Fomularios import ModuloGeneral as gen 
from pandastable import Table
from Fomularios import ModuloGeneral as gen
import Ventana as util_ventana
import pandas as pd

class AñadirProductos():

    def __init__(self,panel_principal, productos,categorías):
        self.barra_superior1 = tk.Frame(panel_principal)
        #self.barra_superior1.columnconfigure(10,)
        self.barra_superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side = tk.BOTTOM, fill="both", expand= True)

        self.controles_barra_superior(productos,categorías)
        self.buscador(productos,categorías)
        self.cuadro_Productos(productos)
        
    def añadirCategoria(self,categorías):  #Cuando se presiona el botón añadir categoría
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
        aceptar = tk.Button(popUp, text = "Aceptar", command = lambda: self.aceptarCategoria(popUp,cajaTexto1,categorías))
        aceptar.grid(row = 2, column = 1)
        gen.cancelar(popUp, 2, 2)

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
    def añadirProducto(self,productos,categorías,Textocaja1 = "no",Textocaja2="no",índice = "No"):
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
        aceptar = tk.Button(popUp, text = "Aceptar", command = lambda: self.aceptarProducto(popUp,cajaTexto1,cajaTexto2,categoria,productos,índice))
        aceptar.grid(row = 2, column = 2)
        gen.cancelar(popUp, 2, 3)
        
    def aceptarProducto(self,popUp,cajaTexto1,cajaTexto2,categoria,productos,índice):
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
                if índice == "No":
                    productos.loc[len(productos)] = [producto, precio, categoria]
                    
                else:
                    productos.loc[índice] = [producto, precio, categoria]
                productos.to_csv("productos.csv")
                print(productos) #Print temporal para ver si funciona correctamente
                popUp.destroy()
            #Refrescar la tabla
            self.table.redraw()
        #Si el precio ingresado no es un número, mostrar error
        except TypeError:
            gen.advertencia("El precio ingresado no es válido. Por favor intente de nuevo", cajaTexto2)

    def controles_barra_superior(self, productos,categorías):
        self.Añadir_Categoria = tk. Button(self.barra_superior1,text="Añadir Categoría", command= lambda: self.añadirCategoria(categorías))
        self.Añadir_Categoria.pack(side=tk.LEFT)
        self.Añadir_Producto = tk.Button(self.barra_superior1, text="Añadir Producto", command = lambda: self.añadirProducto(productos,categorías,Textocaja1 = "no",Textocaja2="no",índice = "No"))
        self.Añadir_Producto.pack(side=tk.LEFT)

    def texto_buscador_productos(self,evento):
        self.buscador_productos.insert(0,"🔎                       Buscar un producto")

    def buscar_producto(self,evento,productos,categorías):
        #Recuperar el texto que se buscó
        busqueda = self.buscador_productos.get()
        #Borrar lo escrito y resetear la caja de texto
        self.buscador_productos.delete(0, tk.END)
        self.buscador_productos.insert(0,"🔎                       Buscar un producto")
        #Buscar el producto en el dataframe
        if busqueda in productos.producto.values:
            self.table.destroy()
            #Si se encuentra el producto obtener el índice
            indice = productos.index[productos["producto"]==busqueda]
            #Crear un dataframe con solo el producto encontrado, y una tabla a partir del dataframe
            producto_encontrado = productos[productos["producto"]==busqueda]
            self.table2 = Table(self.barra_inferior, dataframe= producto_encontrado, showtoolbar= False, showstatusbar= True, editable= False)
            self.table2.show()

            #Crear y mapear el botón editar
            self.editar = tk.Button(self.barra_superior1,text="Editar",command=lambda: self.editar_producto(productos,categorías,indice))
            self.editar.pack()
            #Crear y mapear el botón eliminar
            self.eliminar=tk.Button(self.barra_superior1,text="Eliminar",command=lambda:self.eliminar_producto(productos,indice))
            self.eliminar.pack()
            #Crear y mapear el botón volver
            self.volver= tk.Button(self.barra_superior1, text="Volver",command=lambda:self.regresar(productos))
            self.volver.pack()
        else:
            gen.advertencia("El producto no se ha encontrado")
    
    def editar_producto(self,productos,categorías,indice):
        self.añadirProducto(productos,categorías,Textocaja1 = str(productos["producto"].iloc[indice]),Textocaja2=float(productos["precio"].iloc[indice]),índice = indice)
        self.regresar(productos)
    
    def eliminar_producto(self,productos,indice):
        productos = productos.drop(indice,axis=0).reset_index(drop=True)
        productos.to_csv("productos.csv")
        print(productos)
        gen.advertencia("El producto ha sido eliminado")
        self.regresar(productos)
            
    #Función para volver a la tabla original
    def regresar(self,productos):
        self.table2.destroy()
        self.editar.pack_forget()
        self.eliminar.pack_forget()
        self.volver.pack_forget()
        self.cuadro_Productos(productos)
    
    def buscador(self, productos, categorías):
        #Buscador
        self.buscador_productos = tk.Entry(self.barra_superior1,width=50)
        self.buscador_productos.pack(side = tk.LEFT)
        self.buscador_productos.delete(0, tk.END)
        self.buscador_productos.insert(0,"🔎                       Buscar un producto")
        self.buscador_productos.bind("<FocusIn>", lambda x:gen.borrar_texto(x,self.buscador_productos))
        self.buscador_productos.bind("<FocusOut>", lambda x:self.texto_buscador_productos(x))
        self.buscador_productos.bind("<Return>", lambda x:self.buscar_producto(x,productos,categorías))

 #se crea la tabla de productos
    def cuadro_Productos(self, productos):
        #se indica la tabla con los parametros en el siguente orden "frame donde se coloca, dataframe donde saca los datos, se quita la barra de opciones de la tabla, se muestra las opciones de visualización, se desactiva la función de edición"
        productos = productos[["categoría","producto","precio"]].sort_values(by="categoría")
        self.table = Table(self.barra_inferior, dataframe= productos, showtoolbar= False, showstatusbar= True, editable= False)
        self.table.show()
