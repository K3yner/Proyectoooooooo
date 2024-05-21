import tkinter as tk
from Config import COLOR_CUERPO_PRINCIPAL
from Fomularios import ModuloGeneral as gen 
from Fomularios import ModuloProductos as pr
import pandas as pd

#Crear o abrir el df / csv de productos
try:
    productos = pd.read_csv("productos.csv")
except:
    cosa = {"producto": [], "precio":[], "categoría":[]}
    columnas = ["producto", "precio","categoría"]
    productos = pd.DataFrame(cosa, columns= columnas)
    productos.to_csv("productos.csv")
    productos = pd.read_csv("productos.csv")
#Eliminar la columna inútil de index que tiene el csv >:v
productos = productos.drop(productos.iloc[:,0:1].columns, axis= 1)
categorías = []

class AñadirProductos():

    def __init__(self,panel_principal):
        self.barra_superior1 = tk.Frame(panel_principal)
        self.barra_superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side = tk.BOTTOM, fill="both", expand= True)

        self.controles_barra_superior()
        self.buscador()
        #PRODUCTOS
        #Crear diccionario de productos vacíos
        #productos = {"Sin categoría":{}}

    def controles_barra_superior(self):
        self.Añadir_Categoria = tk. Button(self.barra_superior1,text="Añadir Categoría", command= lambda: pr.añadirCategoria(productos,categorías))
        self.Añadir_Categoria.pack(side=tk.LEFT)
        self.Añadir_Producto = tk.Button(self.barra_superior1, text="Añadir Producto", command = lambda: pr.añadirProducto(productos,categorías))
        self.Añadir_Producto.pack(side=tk.LEFT)

    def buscador(self):
        #Buscador
        self.buscador_productos = tk.Entry(self.barra_superior1,width=50)
        self.buscador_productos.pack(side = tk.LEFT)
        self.buscador_productos.insert(0,"🔎                       Buscar un producto")
        self.buscador_productos.bind("<FocusIn>", lambda x:gen.borrar_texto(x,self.buscador_productos))
        self.buscador_productos.bind("<FocusOut>", lambda x:pr.texto_buscador_productos(x,self.buscador_productos))
        self.buscador_productos.bind("<Return>", lambda x:pr.buscar_producto(self.barra_inferior,x,self.buscador_productos,productos,self))

        