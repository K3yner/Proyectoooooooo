import tkinter as tk
import datetime
import calendar
from util import Ventana as util_ventana
#Función para mostrar un error (sobre lo recuperado de una caja de texto).
#Parámetro "advertencia" = texto del popUp de error
#Parámetro "borrar" = caja de texto que se debe borrar porque es inválida
def advertencia(advertencia,borrar="no"):
    warning = tk.Toplevel()
    warning.config(width=300, height=50)
    util_ventana.centrarVentana(warning, 300, 50)
    warning.grid()
    kaput = tk.Label(warning, text = advertencia)
    kaput.grid()
    if borrar != "no":
        borrar.delete(0,"end")
    
#Botón cancelar para destruir un popUp 
#Parámetro popUp = toplevel que se desea destruir 
def cancelar(popUp, Row, Column,command_cancel="destroy"):
    if command_cancel=="destroy":
        cancelar = tk.Button(popUp, text = "Cancelar", command = popUp.destroy)
    else:
        cancelar = tk.Button(popUp, text = "Cancelar", command = command_cancel)
    cancelar.grid(row= Row, column = Column)
    
def check(boton):
    if boton.cget("text") == "  ":
        boton.configure(text = "✓")
    else:
        boton.configure(text = "  ")
        
def borrar_texto(event,entry):
    entry.delete(0, tk.END)
        
def fecha_letras(fecha):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio" , "julio", "agosto","septiembre","octubre","noviembre","diciembre"]
    string_fecha = str(fecha.day) + " de " + meses[fecha.month-1] + " de " + str(fecha.year)
    return string_fecha
    
def dias_mes():
    # Obtener el año y mes actual
    año_actual = datetime.datetime.now().year
    mes_actual = datetime.datetime.now().month
    # Obtener el número de días en el mes actual
    dias_en_mes = int(calendar.monthrange(año_actual, mes_actual)[1])
    return dias_en_mes