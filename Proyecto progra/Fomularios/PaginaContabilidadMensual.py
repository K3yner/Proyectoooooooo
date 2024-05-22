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
    def __init__(self,panel_principal):
        self.barra_Superior1 = tk.Frame(panel_principal)
        self.barra_Superior1.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_Superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_Inferior = tk.Frame(panel_principal)
        self.barra_Inferior.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_Inferior.pack(side = tk.BOTTOM, fill="both", expand= True)
        
    def controlessuperiores(self):
        self.Añadir_Pago_Mensual.grid(row=2, column=3)
        self.Añadir_Ingreso_Mensual.grid(row=2, column=2)
        self.boton_Mes.grid(row=0, column=0)
        self.fecha_Label["text"] = "Abril"  #Temporal
        self.conta_diaria.grid(row = 8, column = 2)