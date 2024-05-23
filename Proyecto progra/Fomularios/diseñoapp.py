import tkinter as tk
from tkinter import font
#from tkfontawesome import icon_to_image
from tkinter import PhotoImage
from Config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.Ventana as util_ventana
import util.imagenes as util_img
from Fomularios.PaginaEstadísticas import Estadísticas
from Fomularios.Sitioenconstruccion2 import Enconstrucción2
from Fomularios.PaginaAñadirProductos import AñadirProductos
from Fomularios.PaginaContabilidad import ContabilidadDiaria
from Fomularios.PaginaContabilidadMensual import ContaMensual
import pandas as pd

#crear el df/csv de categorías
try:
    categorías = pd.read_csv("categorías.csv")
except:
    cosa = {"categorías": ["Sin categoría"]}
    columnas = ["categorías"]
    categorías = pd.DataFrame(cosa, columns= columnas)
    categorías.to_csv("categorías.csv")
    categorías = pd.read_csv("categorías.csv")
#Eliminar la columna inútil de index que tiene el csv >:v
categorías = categorías.drop(categorías.iloc[:,0:1].columns, axis= 1)

#crear el df / csv de productos
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

#Crear o abrir el df / csv de ventas
try:
    ventas = pd.read_csv("ventas.csv")
except:
    cosa = {"producto": [], "cantidad":[], "ingreso":[],"fecha":[]}
    columnas = ["producto", "cantidad","ingreso","fecha"]

    ventas = pd.DataFrame(cosa, columns= columnas)

    ventas.to_csv("ventas.csv")
    ventas = pd.read_csv("ventas.csv")
#Eliminar la columna inútil de index que tiene el csv >:v
ventas = ventas.drop(ventas.iloc[:,0:1].columns, axis= 1)
#ventas = pd.to_datetime(ventas["fecha"])

#Crear o abrir el df / csv de pagos
try:
    pagos = pd.read_csv("pagos.csv")
except:
    cosa = {"pago": [], "monto":[], "fecha":[],}
    columnas = ["pago", "monto","fecha"]
    pagos = pd.DataFrame(cosa, columns= columnas)
    pagos.to_csv("pagos.csv")
    pagos = pd.read_csv("pagos.csv")
#Eliminar la columna inútil de index que tiene el csv >:v
pagos = pagos.drop(pagos.iloc[:,0:1].columns, axis= 1)

#Crear o abrir el df / csv de pagos recurrentes
try:
    recurrentes = pd.read_csv("recurrentes.csv")
except:
    cosa = {"pago": [], "monto":[]}
    columnas = ["pago", "monto",]
    recurrentes = pd.DataFrame(cosa, columns= columnas)
    recurrentes.to_csv("recurrentes.csv")
    recurrentes= pd.read_csv("recurrentes.csv")
#Eliminar la columna inútil de index que tiene el csv >:v
recurrentes = recurrentes.drop(recurrentes.iloc[:,0:1].columns, axis= 1)

#Crear o abrir el df / csv de inversiones
try:
    inversiones = pd.read_csv("inversiones.csv")
except:
    cosa = {"inversión": [], "monto":[], "fecha":[],}
    columnas = ["inversión", "monto","fecha"]
    inversiones = pd.DataFrame(cosa, columns= columnas)
    inversiones.to_csv("inversiones.csv")
    inversiones = pd.read_csv("inversiones.csv")
#Eliminar la columna inútil de index que tiene el csv >:v
inversiones = inversiones.drop(inversiones.iloc[:,0:1].columns, axis= 1)




#--------------------------------
#Todos esos df fueron creados para poder utilizarse en el resto de modulos del programa.




class pagina(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_ventana()
        self.panels()
        self.controles_barraSuperior()
        self.controles_menuLateral()

    def config_ventana(self):
        #configuración inicial de la ventana
        self.title("prueba")
        w, h = 1024, 600
        #self.geometry("%dx%d+0+0" % (w,h))
        util_ventana.centrarVentana(self,w,h)
    
    def panels(self):
        #crear la barra superior
        self.barra_superior = tk.Frame(
            self, bg= COLOR_BARRA_SUPERIOR, height=50
        )
        self.barra_superior.pack(side = tk.TOP, fill = "both")

        self.menu_lateral = tk.Frame(
            self, bg= COLOR_MENU_LATERAL, width= 150
        )
        self.menu_lateral.pack(side = tk.LEFT, fill= "both", expand= False)
        
        self.cuerpo_principal = tk.Frame(
            self, bg= COLOR_CUERPO_PRINCIPAL, width= 150
        )
        self.cuerpo_principal.pack(side = tk.RIGHT, fill= "both", expand= True)
    
    def controles_barraSuperior(self):
        font_awesome = font.Font(family="FontAwesome", size=12)

        self.menu_boton = tk.Button(self.barra_superior, text= "\uf0c9", font= font_awesome,
                                    command=self.toggle_panel,bd=0, bg= COLOR_BARRA_SUPERIOR, fg="white")
        self.menu_boton.pack(side= tk.LEFT)

    def controles_menuLateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family="FontAwesome", size=15)
        #botones del menú
        self.Boton1 = tk.Button(self.menu_lateral)
        self.Boton2 = tk.Button(self.menu_lateral)
        self.Boton3 = tk.Button(self.menu_lateral)
        self.Boton4 = tk.Button(self.menu_lateral)

        info_botones = [
            ("Contabilidad diaria", "\uf109", self.Boton1, self.abrir_ContabilidadDiaria),
            ("Contabilidad mensual", "\uf03e", self.Boton2, self.abrir_ContabilidadMensual), #Se agregó la pagina de contabilidad mensual (en proceso) y se cambió el orden de los botones
            ("Añadir productos", "\uf007", self.Boton3, self.abrir_Añadir_producto),
            ("Boton4", "\uf013", self.Boton4, self.abrir_Estadísticas),
        ]

        for text, icon, button, comando in info_botones:
            self.configurar_Boton(button, text, icon, font_awesome, ancho_menu, alto_menu,comando)
        
    def configurar_Boton(self,button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f" {icon}  {text}", anchor = "w", font = font_awesome, bd =0,
                      bg = COLOR_MENU_LATERAL, fg = "white", width = ancho_menu, height = alto_menu, command = comando)
        button.pack(side = tk.TOP)
        self.bind_hover_events(button)
        
    def bind_hover_events(self, button):
        #asociar eventos enter y leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event,button))
        button.bind("<Leave>", lambda event: self.on_leave(event,button))

    def on_enter(self, event, button):
        #cambiar color del boton
        button.config(bg = COLOR_MENU_CURSOR_ENCIMA, fg = "white")

    def on_leave(self, event, button):
        #cambiar color del boton
        button.config(bg = COLOR_MENU_LATERAL, fg = "white")
    
    def toggle_panel(self):
        #alterar visivilidad del menú
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side = tk.LEFT, fill = "y")

    def abrir_Estadísticas(self):
        self.limpiar_panel(self.cuerpo_principal)
        Estadísticas(self.cuerpo_principal,ventas,pagos,inversiones)

    #Función para abrir la pestaña de productos    
    def abrir_Añadir_producto(self):
        self.limpiar_panel(self.cuerpo_principal)
        AñadirProductos(self.cuerpo_principal, productos,categorías) #se envía el df productos para crear su respectiva tabla
    
    #función para abrir la pestaña de contabilidad diaria
    def abrir_ContabilidadDiaria(self):
        self.limpiar_panel(self.cuerpo_principal)
        ContabilidadDiaria(self.cuerpo_principal, productos, ventas, pagos, recurrentes, inversiones) # se envían lso df para su posterior uso
        ## el df de ventas es usado en la construcción de la tabla de contabilidad

    #función para abrir la pestaña de contabilidad mensual
    def abrir_ContabilidadMensual(self):
        self.limpiar_panel(self.cuerpo_principal)
        ContaMensual(self.cuerpo_principal, productos, ventas, pagos, recurrentes, inversiones)


    def abrir_construccion2(self):
        self.limpiar_panel(self.cuerpo_principal)
        Enconstrucción2(self.cuerpo_principal)
    
    ##función para limpiar panel
    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()
