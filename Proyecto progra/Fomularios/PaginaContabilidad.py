
import tkinter as tk
from tkinter import ttk
from Config import COLOR_CUERPO_PRINCIPAL
from Fomularios import ModuloGeneral as gen 
from Fomularios import ModuloContabilidad as cnt
from Fomularios.CuadroConta import cuadro
from tkcalendar import Calendar
import datetime
import pandas as pd
import os
from pandastable import Table

#Crear o abrir el df / csv de productos
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




class ContabilidadDiaria():

    def __init__(self,panel_principal):
        self.barra_superior1 = tk.Frame(panel_principal)
        self.barra_superior1.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_inferior.pack(side = tk.BOTTOM, fill="both", expand= True)
        self.controles_barra_superior()
        
        self.cuadro_ventasDiarias()
        
        
        
 


    def controles_barra_superior(self):
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
        
        def cambiarA_mensual():
            #Por ahora estoy borrando y recolocando los botones, pero luego mejor
            #creemos subventanas para diario y mensual
            self.Añadir_Ingreso_Diario.grid_forget()
            self.Añadir_Pago_Diario.grid_forget()
            self.boton_Fecha.grid_forget()
            self.conta_mensual.grid_forget()
            self.Añadir_Pago_Mensual.grid(row=2, column=3)
            self.Añadir_Ingreso_Mensual.grid(row=2, column=2)
            self.boton_Mes.grid(row=0, column=0)
            self.fecha_Label["text"] = "Abril"  #Temporal
            self.conta_diaria.grid(row = 8, column = 2)
        
        self.conta_mensual = tk.Button(self.barra_superior1,text="Mensual",command = cambiarA_mensual)
        self.conta_mensual.grid(row=8, column = 2)
        
        def cambiarA_diario():
            #Por ahora estoy borrando los botones, pero luego mejor
            #creemos subventanas para diario y mensual
            self.Añadir_Pago_Mensual.grid_forget()
            self.Añadir_Ingreso_Mensual.grid_forget()
            self.boton_Mes.grid_forget()
            self.conta_diaria.grid_forget()
            self.Añadir_Ingreso_Diario.grid(row=2, column=1)
            self.Añadir_Pago_Diario.grid(row=2, column=2)
            self.boton_Fecha.grid(row=0,column=0)
            self.fecha_Label["text"] = gen.fecha_letras(datetime.date.today())
            self.conta_mensual.grid(row=8, column = 2)
            
        #Botones de la conta mensual
        self.Añadir_Ingreso_Mensual = tk. Button(self.barra_superior1, text="Añadir Ingreso", command= lambda: cnt.añadirIngreso(ventas,productos,boton_fecha=True))
        self.Añadir_Pago_Mensual = tk. Button(self.barra_superior1, text="Añadir Pago", command= lambda: cnt.añadirPago(pagos,inversiones,recurrentes,boton_fecha=True))
        self.boton_Mes = tk.Button(self.barra_superior1, text="Mes: ", command = cnt.mes)
        self.conta_diaria = tk.Button(self.barra_superior1, text="Diario", command = cambiarA_diario)
    
    #creación de cuadro de ventas
    def cuadro_ventasDiarias(self):
        #se indica la tabla con los parametros en el siguente orden "frame donde se coloca, dataframe donde saca los datos, se quita la barra de opciones de la tabla, se muestra las opciones de visualización, se desactiva la función de edición"
        #### NOTA PARA MAR: ¡No toques los parametros que estan en False! No se como funcionan y no hay tiempo para usarlos
        self.table = Table(self.barra_inferior, dataframe= ventas, showtoolbar= False, showstatusbar= True, editable= False)
        self.table.show()