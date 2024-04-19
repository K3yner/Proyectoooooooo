import tkinter as tk
from tkcalendar import Calendar
from from Fomularios import ModuloGeneral as gen
import datetime

class calendario(tk.Toplevel):
    def __init__(self):
        super().__init__()
        #Botón Fecha
        fecha = datetime.date.today()
        #Colocar el popUP
        self.calendario = tk.Toplevel(self)
        self.calendario.title("Seleccionar fecha") #Título
        #Ocultar popUp
        self.calendario.withdraw()
        #Crear calendario
        cal = Calendar(calendario,locale='es_ES', selectmode="day",maxdate=datetime.date.today())
        #Set fecha incial
        string_fecha = gen.fecha_letras(fecha)