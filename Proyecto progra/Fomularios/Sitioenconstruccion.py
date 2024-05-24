import tkinter as tk
from Config import COLOR_CUERPO_PRINCIPAL
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

class Estadísticas():

    def __init__(self, panel_principal,ventas,pagos,inversiones):
        self.panel_principal = panel_principal

        self.barra_superior = tk.Frame(self.panel_principal)
        self.barra_superior.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=10)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)


        self.panel_principal.grid_columnconfigure(0, weight=1)
        self.panel_principal.grid_rowconfigure(0, weight=0)
        self.panel_principal.grid_rowconfigure(1, weight=1)

        self.barra_superior.grid_columnconfigure(0, weight=1)
        self.barra_inferior.grid_columnconfigure(0, weight=1)
        self.barra_inferior.grid_columnconfigure(1, weight=1)
        self.barra_inferior.grid_columnconfigure(2, weight=1)
        self.barra_inferior.grid_rowconfigure(0, weight=1)

        self.Titulo = tk.Label(self.barra_superior, text= "Proporción de productos vendidos")
        self.Titulo.config(fg="#222d33", font= ("Arial", 30), bg = COLOR_CUERPO_PRINCIPAL)
        self.Titulo.grid(row = 0, column = 0, padx=10, pady=10, sticky=tk.N)
        self.productos_Vendidos(ventas)

        # Subtítulos y gráficos
        self.Titulo1 = tk.Label(self.barra_inferior, text="Por cantidad")
        self.Titulo1.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
        self.Titulo1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

        self.Titulo2 = tk.Label(self.barra_inferior, text="Por ingreso")
        self.Titulo2.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
        self.Titulo2.grid(row=0, column=2, padx=10, pady=10, sticky=tk.N)

        self.productos_Vendidos(ventas)

        self.Titulo = tk.Label(self.barra_inferior, text= "Ventas")
        self.Titulo.config(fg="#222d33", font= ("Arial", 30), bg = COLOR_CUERPO_PRINCIPAL)
        self.Titulo.grid(row = 2, column = 0, padx=10, pady=10, sticky=tk.N)
        self.Ventas()

    def productos_Vendidos(self,ventas):

        #PIE CHART DE PRODUCTOS MÁS VENDIDOS (1)
        productos = ventas.value_counts(ventas["producto"]).reset_index()["producto"]
        cantidades = []
        for producto in productos:
            cantidades.append(ventas[ventas["producto"]==producto]["cantidad"].sum())

        self.productosXcantidad = Figure(figsize=(5,4),dpi=80)
        self.productosXcantidad.add_subplot().pie(cantidades,labels=productos,autopct=lambda pct: int(pct/100.*sum(cantidades)))
        canvas1 = FigureCanvasTkAgg(self.productosXcantidad, master=self.barra_inferior)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=1,column=0, sticky=tk.NSEW, padx=10, pady=10)

        #PIE CHART DE PRODUCTOS CON MÁS INGRESOS (2)
        ingreso = []
        for producto in productos:
            ingreso.append(ventas[ventas["producto"]==producto]["ingreso"].sum())

        self.productosXingreso = Figure(figsize=(5,4),dpi=80)
        self.productosXingreso.add_subplot().pie(ingreso,labels=productos,autopct=lambda pct: "Q." + str(round(float(pct/100.*sum(ingreso)),2)))
        canvas2 = FigureCanvasTkAgg(self.productosXingreso, master=self.barra_inferior)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=1,column=2,)

        
    def Ventas(self):

        self.Titulo3 = tk.Label(self.barra_superior, text="Ventas")
        self.Titulo3.config(fg="#222d33", font=("Arial", 20), bg=self.COLOR_CUERPO_PRINCIPAL)
        self.Titulo3.grid(row=2, column=0, pady=10, padx=10)

        self.b = Figure(figsize=(5, 4), dpi=80)

        # Crear el canvas de Matplotlib y agregarlo a la barra inferior
        canvas3 = FigureCanvasTkAgg(self.b, master=self.barra_inferior)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=3, column=0, pady=10, padx=10)