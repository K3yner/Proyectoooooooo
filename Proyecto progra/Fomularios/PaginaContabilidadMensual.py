import tkinter as tk
from tkinter import ttk
from Config import COLOR_CUERPO_PRINCIPAL
from Fomularios import ModuloGeneral as gen 
from Fomularios import ModuloContabilidad as cnt
from tkcalendar import Calendar
import datetime
import pandas as pd
import os
from pandastable import Table



class ContaMensual():
    def __init__(self,panel_principal, productos, ventas, pagos, recurrentes, inversiones):
        self.barra_Superior1 = tk.Frame(panel_principal)
        self.barra_Superior1.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_Superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_Inferior = tk.Frame(panel_principal)
        self.barra_Inferior.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_Inferior.pack(side = tk.BOTTOM, fill="both", expand= True)
        
        self.controlessuperiores(productos, ventas, pagos, recurrentes, inversiones)
        self.cuadro_ventasMensuales(ventas)
        
    def controlessuperiores(self, productos, ventas, pagos, recurrentes, inversiones):

        global fecha
        fecha = datetime.date.today()
        #Botones de la contabilidad diaria
        self.boton_Fecha = tk.Button(self.barra_Superior1, text = "Fecha:", command= lambda: cnt.mostrar_calendario(self.fecha_Label))
        self.boton_Fecha.grid(row=0,column=0)
        string_fecha = gen.fecha_letras(fecha)
        self.fecha_Label = tk.Label(self.barra_Superior1,text=string_fecha)
        self.fecha_Label.grid(row=0,column=1)

        self.Añadir_Ingreso_Mensual = tk. Button(self.barra_Superior1, text="Añadir Ingreso", command= lambda: cnt.añadirIngreso(ventas,productos,boton_fecha=True))
        self.Añadir_Ingreso_Mensual.grid(row=2, column=2)
        self.Añadir_Pago_Mensual = tk. Button(self.barra_Superior1, text="Añadir Pago", command= lambda: cnt.añadirPago(pagos,inversiones,recurrentes,boton_fecha=True))
        self.Añadir_Pago_Mensual.grid(row=2, column=3)
        self.boton_Mes = tk.Button(self.barra_Superior1, text="Mes: ", command = cnt.mes)
        self.boton_Mes.grid(row=0, column=0)

    def cuadro_ventasMensuales(self, ventas):
        self.table = Table(self.barra_Inferior, dataframe= ventas, showtoolbar= False, showstatusbar= True, editable= False)
        self.table.show()