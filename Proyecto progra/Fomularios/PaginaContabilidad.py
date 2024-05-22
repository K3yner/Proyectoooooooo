
import tkinter as tk
from tkinter import ttk
from Config import COLOR_CUERPO_PRINCIPAL
from Fomularios import ModuloGeneral as gen 
from Fomularios import ModuloContabilidad as cnt
from tkcalendar import Calendar
import datetime
import os
from pandastable import Table #necesario para las tablas





class ContabilidadDiaria():

    def __init__(self,panel_principal, productos, ventas, pagos, recurrentes, inversiones):
        self.barra_superior1 = tk.Frame(panel_principal)
        self.barra_superior1.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_inferior.pack(side = tk.BOTTOM, fill="both", expand= True)
        self.controles_barra_superior(productos, ventas, pagos, recurrentes, inversiones)
        
        self.cuadro_ventasDiarias(ventas)
        
        
        
 


    def controles_barra_superior(self, productos, ventas, pagos, recurrentes, inversiones):
        global fecha
        fecha = datetime.date.today()
        #Botones de la contabilidad diaria
        self.boton_Fecha = tk.Button(self.barra_superior1, text = "Fecha:", command= lambda: cnt.mostrar_calendario(self.fecha_Label))
        self.boton_Fecha.grid(row=0,column=0)
        string_fecha = gen.fecha_letras(fecha)
        self.fecha_Label = tk.Label(self.barra_superior1,text=string_fecha)
        self.fecha_Label.grid(row=0,column=1)
        
        self.Añadir_Ingreso_Diario = tk. Button(self.barra_superior1, text="Añadir Ingreso",command= lambda: cnt.añadirIngreso(ventas,productos))
        self.Añadir_Ingreso_Diario.grid(row=2, column=1)
        self.Añadir_Pago_Diario = tk. Button(self.barra_superior1, text="Añadir Pago", command= lambda: cnt.añadirPago(pagos,inversiones,recurrentes))
        self.Añadir_Pago_Diario.grid(row=2, column=2)
        
    
    #creación de cuadro de ventas
    def cuadro_ventasDiarias(self, ventas):
        cuadro = ventas[ventas["fecha"]== str(fecha)]
        #se indica la tabla con los parametros en el siguente orden "frame donde se coloca, dataframe donde saca los datos, se quita la barra de opciones de la tabla, se muestra las opciones de visualización, se desactiva la función de edición"
        #### NOTA PARA MAR: ¡No toques los parametros que estan en False! No se como funcionan y no hay tiempo para usarlos
        self.table = Table(self.barra_inferior, dataframe= cuadro, showtoolbar= False, showstatusbar= True, editable= False)
        self.table.show()