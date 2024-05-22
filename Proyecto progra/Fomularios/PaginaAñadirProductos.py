import tkinter as tk
from Config import COLOR_CUERPO_PRINCIPAL
from Fomularios import ModuloGeneral as gen 
from Fomularios import ModuloProductos as pr
from pandastable import Table



class AñadirProductos():

    def __init__(self,panel_principal, productos):
        self.barra_superior1 = tk.Frame(panel_principal)
        self.barra_superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side = tk.BOTTOM, fill="both", expand= True)

        self.controles_barra_superior(productos)
        self.buscador(productos)
        
        self.cuadro_Productos(productos)
        
        #PRODUCTOS
        #Crear diccionario de productos vacíos
        #productos = {"Sin categoría":{}}

    def controles_barra_superior(self, productos):
        self.Añadir_Categoria = tk. Button(self.barra_superior1,text="Añadir Categoría", command= lambda: pr.añadirCategoria(productos,productos["categoría"]))
        self.Añadir_Categoria.pack(side=tk.LEFT)
        self.Añadir_Producto = tk.Button(self.barra_superior1, text="Añadir Producto", command = lambda: pr.añadirProducto(productos,productos["categoría"]))
        self.Añadir_Producto.pack(side=tk.LEFT)

        
    
    
    def buscador(self, productos):
        #Buscador
        self.buscador_productos = tk.Entry(self.barra_superior1,width=50)
        self.buscador_productos.pack(side = tk.LEFT)
        self.buscador_productos.insert(0,"🔎                       Buscar un producto")
        self.buscador_productos.bind("<FocusIn>", lambda x:gen.borrar_texto(x,self.buscador_productos))
        self.buscador_productos.bind("<FocusOut>", lambda x:pr.texto_buscador_productos(x,self.buscador_productos))
        self.buscador_productos.bind("<Return>", lambda x:pr.buscar_producto(self.barra_inferior,x,self.buscador_productos,productos,self))



    #se crea la tabla de productos
    def cuadro_Productos(self, productos):
        #se indica la tabla con los parametros en el siguente orden "frame donde se coloca, dataframe donde saca los datos, se quita la barra de opciones de la tabla, se muestra las opciones de visualización, se desactiva la función de edición"
        #### NOTA PARA MAR: ¡No toques los parametros que estan en False! No se como funcionan y no hay tiempo para usarlos
        self.table = Table(self.barra_inferior, dataframe= productos, showtoolbar= False, showstatusbar= True, editable= False)
        self.table.show()
        

        