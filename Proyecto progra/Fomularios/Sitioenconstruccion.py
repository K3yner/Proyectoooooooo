import tkinter as tk
from Config import COLOR_CUERPO_PRINCIPAL
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import datetime

class Estadísticas():

    def __init__(self, panel_principal,ventas,pagos,inversiones):
        self.meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        ventas["fecha"] = pd.to_datetime(ventas["fecha"])   
        ventas["fecha"] = ventas["fecha"].dt.date
        pagos["fecha"] = pd.to_datetime(pagos["fecha"])   
        pagos["fecha"] = pagos["fecha"].dt.date

        self.panel_principal = panel_principal

        self.barra_superior = tk.Frame(self.panel_principal)
        self.barra_superior.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=10)
        self.grafica = tk.StringVar(self.barra_superior,"Estadísticas")
        self.opciones = ["Productos vendidos", "Ventas", "Utilidad","Retorno de inversión"]
        menu = tk.OptionMenu(self.barra_superior, self.grafica, *self.opciones, command = lambda x: self.estadisticas(x,ventas,pagos)) 
        menu.grid(row=0,column=0)

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
        self.barra_inferior.grid_rowconfigure(1, weight=1)
        self.barra_inferior.grid_rowconfigure(2, weight=1)
        self.barra_inferior.grid_rowconfigure(3, weight=1)
    
    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def estadisticas(self,x,ventas,pagos):
        if x == "Productos vendidos":
            self.limpiar_panel(self.barra_inferior)
            self.Titulo = tk.Label(self.barra_inferior, text= "Proporción de productos vendidos")
            self.Titulo.config(fg="#222d33", font= ("Arial", 30), bg = COLOR_CUERPO_PRINCIPAL)
            self.Titulo.grid(row = 0, column = 0, padx=10, pady=10, sticky=tk.EW, columnspan=3)
            # Subtítulos y gráficos
            self.Titulo1 = tk.Label(self.barra_inferior, text="Por cantidad")
            self.Titulo1.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
            self.Titulo1.grid(row=1, column=0, padx=10, pady=10, sticky=tk.N)

            self.Titulo2 = tk.Label(self.barra_inferior, text="Por ingreso")
            self.Titulo2.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
            self.Titulo2.grid(row=1, column=2, padx=10, pady=10, sticky=tk.N)
            self.productos_Vendidos(ventas)

        if x == "Ventas": 
            self.limpiar_panel(self.barra_inferior)
            self.Titulo = tk.Label(self.barra_inferior, text= "Ventas")
            self.Titulo.config(fg="#222d33", font= ("Arial", 30), bg = COLOR_CUERPO_PRINCIPAL)
            self.Titulo.grid(row = 0, column = 0, padx=10, pady=10, sticky=tk.EW, columnspan=3)

            self.Titulo1 = tk.Label(self.barra_inferior, text="Mensual")
            self.Titulo1.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
            self.Titulo1.grid(row=1, column=0, padx=10, pady=10, sticky=tk.N)

            self.Titulo2 = tk.Label(self.barra_inferior, text="Anual")
            self.Titulo2.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
            self.Titulo2.grid(row=1, column=2, padx=10, pady=10, sticky=tk.N)

            self.Ventas(ventas)

        if x == "Utilidad":
            self.limpiar_panel(self.barra_inferior)
            self.Titulo = tk.Label(self.barra_inferior, text= "Utilidades")
            self.Titulo.config(fg="#222d33", font= ("Arial", 30), bg = COLOR_CUERPO_PRINCIPAL)
            self.Titulo.grid(row = 0, column = 0, padx=10, pady=10, sticky=tk.EW, columnspan=3)
            self.utilidad(ventas,pagos)
        if x == "Retorno de inversión":
            print("Hola")

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
        canvas1.get_tk_widget().grid(row=2,column=0, sticky=tk.E, padx=10, pady=10)

        #PIE CHART DE PRODUCTOS CON MÁS INGRESOS (2)
        ingreso = []
        for producto in productos:
            ingreso.append(ventas[ventas["producto"]==producto]["ingreso"].sum())

        self.productosXingreso = Figure(figsize=(5,4),dpi=80)
        self.productosXingreso.add_subplot().pie(ingreso,labels=productos,autopct=lambda pct: "Q." + str(round(float(pct/100.*sum(ingreso)),2)))
        canvas2 = FigureCanvasTkAgg(self.productosXingreso, master=self.barra_inferior)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=2,column=2, sticky=tk.W, padx=10,pady=10)

    def montoXmes(self,df,columna):
        df_año = df[df["fecha"].apply(lambda x:x.year) == datetime.date.today().year]
        df_año["mes"] = df_año["fecha"].apply(lambda x:x.month)
        meses_df = df_año.value_counts(df_año["mes"]).reset_index()["mes"]
        montos_año = [0,0,0,0,0,0,0,0,0,0,0,0]
        for x in meses_df:
            montos_año[x-1] = df_año[df_año["mes"]==x][columna].sum()
        return montos_año   
    
    def Ventas(self,ventas):
        #Ingresos mensuales
        mes = datetime.date.today().month
        self.ventas_mes = ventas[ventas["fecha"].apply(lambda x:x.month) == mes]

        fechas = self.ventas_mes.value_counts(ventas["fecha"]).reset_index()["fecha"].sort_values()
        self.ingresos_mes = []
        for fecha in fechas:
            self.ingresos_mes.append(self.ventas_mes[self.ventas_mes["fecha"]==fecha]["ingreso"].sum())

        self.ventas_mensuales = Figure(figsize=(5,4),dpi=100)
        ej = self.ventas_mensuales.add_subplot()
        ej.plot(fechas.apply(lambda x: x.day),self.ingresos_mes,marker='o')
        ej.set_xlabel("Mayo")
        ej.set_ylabel("Ingreso")
        canvas4 = FigureCanvasTkAgg(self.ventas_mensuales, master=self.barra_inferior)
        canvas4.draw()
        canvas4.get_tk_widget().grid(row=2, column=0, pady=10, padx=10, sticky=tk.NSEW)
        
        #Ingresos anuales
        self.ingresos_año = self.montoXmes(ventas,"ingreso")
        self.ventas_anuales = Figure(figsize=(5,4),dpi=80)
        ax = self.ventas_anuales.add_subplot()
        ax.plot(self.meses,self.ingresos_año,marker='o')
        ax.set_xlabel("Mes")
        ax.set_ylabel("ingreso")
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        canvas3 = FigureCanvasTkAgg(self.ventas_anuales, master=self.barra_inferior)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=2, column=2, pady=10, padx=10, sticky=tk.NSEW)

    def utilidad(self,ventas,pagos):
        ingresos_año = self.montoXmes(ventas,"ingreso")
        egresos_año = self.montoXmes(pagos,"monto")
        lista = []
        for x in range(12):
            lista.append(ingresos_año[x-1] - egresos_año[x-1])
        self.utilidad_graf = Figure(figsize=(5,4),dpi=80)
        ax = self.utilidad_graf.add_subplot()
        ax.plot(self.meses,lista,marker='o')
        ax.set_xlabel("Mes")
        ax.set_ylabel("Utilidad")
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

        canvas = FigureCanvasTkAgg(self.utilidad_graf, master=self.barra_inferior)
        #canvas.config(height = 100)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2,column=1, pady=10, padx=10, sticky=tk.EW)

        
