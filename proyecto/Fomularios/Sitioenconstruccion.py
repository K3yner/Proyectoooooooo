import tkinter as tk
from Config import COLOR_CUERPO_PRINCIPAL

class Enconstrucción():

    def __init__(self, panel_principal, logo):
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side= tk.TOP, fill= "x", expand= False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side = tk.BOTTOM, fill="both", expand= True)

        self.Titulo = tk.Label(self.barra_superior, text= "Página en construcción")
        self.Titulo.config(fg="#222d33", font= ("Arial", 30), bg = COLOR_CUERPO_PRINCIPAL)
        self.Titulo.pack(side = tk.TOP, fill = "both", expand=True)

        self.imagen = tk.Label(self.barra_inferior, image = logo)
        self.imagen.place(x=0,y=0, relheight=1, relwidth=1)
        self.imagen.pack(fg = "#fff", font=("Roboto", 10), bg = COLOR_CUERPO_PRINCIPAL)