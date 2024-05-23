import tkinter as tk
from Config import COLOR_CUERPO_PRINCIPAL
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

class Estadísticas():

    def __init__(self, panel_principal,ventas,pagos,inversiones):
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side= tk.TOP, fill= "x", expand= False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side = tk.BOTTOM, fill="both", expand= True)

        self.barra_inferior.columnconfigure(0, weight=1)
        self.barra_inferior.columnconfigure(1, weight=1)
        self.barra_inferior.columnconfigure(2, weight=1)
        self.barra_inferior.columnconfigure(3, weight=1)
        self.barra_inferior.columnconfigure(4, weight=1)
        self.barra_inferior.rowconfigure(0, weight=1)
        self.barra_inferior.rowconfigure(1, weight=1)
        self.barra_inferior.rowconfigure(2, weight=1)
        self.barra_inferior.rowconfigure(3, weight=1)
        self.barra_inferior.rowconfigure(4, weight=1)

        self.Titulo = tk.Label(self.barra_superior, text= "Proporción de productos vendidos")
        self.Titulo.config(fg="#222d33", font= ("Arial", 30), bg = COLOR_CUERPO_PRINCIPAL)
        self.Titulo.grid(row = 0, column = 0, columnspan=5, padx=5, pady=5)
        self.productos_Vendidos(ventas)

        self.Titulo2 = tk.Label(self.barra_superior, text= "Ventas")
        self.Titulo2.config(fg="#222d33", font= ("Arial", 30), bg = COLOR_CUERPO_PRINCIPAL)
        self.Titulo2.grid(row = 2, column = 0, columnspan=2, sticky=tk.EW)
        self.Ventas()

    def productos_Vendidos(self,ventas):

        #PIE CHART DE PRODUCTOS MÁS VENDIDOS (1)
        self.Titulo1 = tk.Label(self.barra_superior, text= "Por cantidad")
        self.Titulo1.config(fg="#222d33", font= ("Arial", 20), bg = COLOR_CUERPO_PRINCIPAL)
        self.Titulo1.grid(row = 1, column = 0, columnspan=2, sticky=tk.EW, padx=5, pady=5)

        productos = ventas.value_counts(ventas["producto"]).reset_index()["producto"]
        cantidades = []
        for producto in productos:
            cantidades.append(ventas[ventas["producto"]==producto]["cantidad"].sum())

        self.productosXcantidad = Figure(figsize=(5,4),dpi=80)
        self.productosXcantidad.add_subplot().pie(cantidades,labels=productos,autopct=lambda pct: int(pct/100.*sum(cantidades)))
        canvas1 = FigureCanvasTkAgg(self.productosXcantidad, master=self.barra_inferior)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=1,column=2)

        #PIE CHART DE PRODUCTOS CON MÁS INGRESOS (2)
        self.Titulo2 = tk.Label(self.barra_superior, text= "Por ingreso")
        self.Titulo2.config(fg="#222d33", font= ("Arial", 20), bg = COLOR_CUERPO_PRINCIPAL)
        self.Titulo2.grid(row = 1, column = 1)
        ingreso = []
        for producto in productos:
            ingreso.append(ventas[ventas["producto"]==producto]["ingreso"].sum())

        self.productosXingreso = Figure(figsize=(5,4),dpi=80)
        self.productosXingreso.add_subplot().pie(ingreso,labels=productos,autopct=lambda pct: "Q." + str(round(float(pct/100.*sum(ingreso)),2)))
        canvas2 = FigureCanvasTkAgg(self.productosXingreso, master=self.barra_inferior)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=2,column=1)


    def Ventas(self):

        self.Titulo3 = tk.Label(self.barra_superior, text= "Ventas")
        self.Titulo3.config(fg="#222d33", font= ("Arial", 20), bg = COLOR_CUERPO_PRINCIPAL)
        self.Titulo3.grid(row = 4, column = 1)

        self.b = Figure(figsize=(5,4),dpi=80)
        self.b.add_subplot()

        canvas3 = FigureCanvasTkAgg(self.b, master=self.barra_inferior)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=3,column=2)

