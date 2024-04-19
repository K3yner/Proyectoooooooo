
import tkinter as tk
from tkinter import ttk
from Config import COLOR_CUERPO_PRINCIPAL
from Fomularios import PaginaAñadirProductos as ppro
from Fomularios import ModuloGeneral as gen 
from Fomularios import ModuloContabilidad as cnt
from Fomularios.CuadroConta import cuadro
from tkcalendar import Calendar
import datetime
from tabulate import tabulate 




class ContabilidadDiaria():

    def __init__(self,panel_principal):
        self.barra_superior1 = tk.Frame(panel_principal)
        self.barra_superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side = tk.BOTTOM, fill="both", expand= True)
        self.controles_barra_superior()
 



    def controles_barra_superior(self):
        fecha = datetime.date.today()

        self.boton_Fecha = tk.Button(self.barra_superior1, text = "Fecha:", command= lambda: cnt.mostrar_calendario(self.fecha_Label))
        self.boton_Fecha.pack(side=tk.LEFT)
        string_fecha = gen.fecha_letras(fecha)
        self.fecha_Label = tk.Label(self.barra_superior1,text=string_fecha)
        self.fecha_Label.pack(side= tk.LEFT)

        self.Añadir_Ingreso_Diario = tk. Button(self.barra_inferior, text="Añadir Ingreso",command= lambda: cnt.añadirIngreso(cnt.ventas,ppro.productos))
        self.Añadir_Ingreso_Diario.grid(row=2, column=1)
        self.Añadir_Pago_Diario = tk. Button(self.barra_inferior, text="Añadir Pago", command= lambda: cnt.añadirPago(cnt.inversiones))
        self.Añadir_Pago_Diario.grid(row=2, column=2)
    """"
        def abrir_cuadro(self):
            cuadro = ttk.Treeview(self.barra_inferior, columns=("col1", "col2", "col3"))
            w = 80
            columnas =["#0","col1", "col2", "col3"]
            for i in range(0,len(columnas)-1):
                cuadro.column(columnas[i], width=w, anchor="center")
            nombres_columnas = ["Ventas", "Pagos", "Ingresos", "Egresos"]
            for i in range(0,len(columnas)-1):
                cuadro.heading(columnas[i], text= nombres_columnas[i], anchor= "center")
    """
    """def cuadro():
        cuadro_ingresos = []
        for i in range(0,len(cnt.ventas)-1):
            cuadro_ingresos.append(cnt.ventas[i])"""