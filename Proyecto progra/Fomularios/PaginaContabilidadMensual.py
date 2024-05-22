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

class ContaMensual():
    def __init__(self,panel_principal):
        self.barra_Superior1 = tk.Frame(panel_principal)
        self.barra_Superior1.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_Superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_Inferior = tk.Frame(panel_principal)
        self.barra_Inferior.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_Inferior.pack(side = tk.BOTTOM, fill="both", expand= True)