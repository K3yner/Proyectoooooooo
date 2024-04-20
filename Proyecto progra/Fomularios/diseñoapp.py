import tkinter as tk
from tkinter import font
#from tkfontawesome import icon_to_image
from tkinter import PhotoImage
from Config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.Ventana as util_ventana
import util.imagenes as util_img
from Fomularios.Sitioenconstruccion import Enconstrucción
from Fomularios.Sitioenconstruccion2 import Enconstrucción2
from Fomularios.PaginaAñadirProductos import AñadirProductos
from Fomularios.PaginaContabilidad import ContabilidadDiaria


class pagina(tk.Tk):
    def __init__(self):
        super().__init__()
        self.img_sitio_construccion = util_img.leer_imagen("./Imagenes/sitio_construccion.png", (300,300))
        self.img_sitio_construccion2 = util_img.leer_imagen("./Imagenes/grua.jpg", (300,300))
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
            ("Añadir productos", "\uf007", self.Boton2, self.abrir_Añadir_producto),
            ("Boton3", "\uf03e", self.Boton3, self.abrir_construccion),
            ("Boton4", "\uf013", self.Boton4, self.abrir_construccion2),
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

    def abrir_construccion(self):
        self.limpiar_panel(self.cuerpo_principal)
        Enconstrucción(self.cuerpo_principal, self.img_sitio_construccion)
    
    def abrir_Añadir_producto(self):
        self.limpiar_panel(self.cuerpo_principal)
        AñadirProductos(self.cuerpo_principal)
    
    def abrir_ContabilidadDiaria(self):
        self.limpiar_panel(self.cuerpo_principal)
        ContabilidadDiaria(self.cuerpo_principal)

    def abrir_construccion2(self):
        self.limpiar_panel(self.cuerpo_principal)
        Enconstrucción2(self.cuerpo_principal, self.img_sitio_construccion2)
    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()
