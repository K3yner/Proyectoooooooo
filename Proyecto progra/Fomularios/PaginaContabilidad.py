
import tkinter as tk
from tkinter import ttk
from Config import COLOR_CUERPO_PRINCIPAL
from Fomularios import ModuloGeneral as gen 
from tkcalendar import Calendar
import datetime
import os
from pandastable import Table, TableModel #necesario para las tablas
import pandas as pd
from datetime import date
from util import Ventana as util_ventana




class ContabilidadDiaria():

    def __init__(self,panel_principal, productos, ventas, pagos, recurrentes, inversiones):
        self.barra_superior1 = tk.Frame(panel_principal)
        self.barra_superior1.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_superior1.pack(side= tk.TOP, fill= "x", expand=False)

        self.barra_media = tk.Frame(panel_principal)
        self.barra_media.config(bg= COLOR_CUERPO_PRINCIPAL)
        self.barra_media.pack(side = tk.TOP, fill="both", expand= False)
        
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.config(bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_inferior.pack(side=tk.BOTTOM, fill = "both", expand=True)
        
        self.controles_barra_superior(productos, ventas, pagos, recurrentes, inversiones)
        
        self.cuadro_ventasDiarias(ventas)
        self.cuadro_pagosDiarios(pagos)
        
    #FUNCIONES PARA DEFINIR LA FECHA
    def mostrar_calendario(self,fecha_Label,pagos,ventas,actualizar=True):
        #Colocar el popUP
        self.calendario = tk.Toplevel()
        self.calendario.title("Seleccionar fecha") #Título
        #Crear calendario
        self.cal = Calendar(self.calendario,locale='es_ES', selectmode="day",maxdate=datetime.date.today())
        #Colocar calendario
        self.cal.pack()
        #Botón seleccionar fecha
        self.seleccionar = tk.Button(self.calendario, text="Seleccionar Fecha", command=lambda:self.seleccionar_fecha(pagos,ventas,
        actualizar,self.fecha_Label))
        self.seleccionar.pack()

    def seleccionar_fecha(self,pagos,ventas,actualizar,fecha_Label="no"):
        self.fecha = self.cal.selection_get()
        string_fecha = gen.fecha_letras(self.fecha)
        if fecha_Label != "no":
            fecha_Label["text"] = string_fecha
        self.calendario.withdraw()
        self.seleccionar.destroy()
        if actualizar == True:
            Fecha = datetime.date(self.fecha.year,self.fecha.month,self.fecha.day)
            self.cuadroPagos = pagos[pagos["fecha"]== Fecha]
            self.cuadroVentas = ventas[ventas["fecha"]== Fecha]
            ventas1 = pd.read_csv("ventas.csv") # Se crea un df temporal para actualizar la tabla
            pagos1 = pd.read_csv("pagos.csv")
            #Eliminar la columna inútil de index que tiene el csv >:v
            ventas1 = ventas1.drop(ventas1.iloc[:,0:1].columns, axis= 1)
            pagos1 = pagos1.drop(pagos1.iloc[:,0:1].columns, axis= 1)
            self.cuadro_ventasDiarias(ventas1)
            self.cuadro_pagosDiarios(pagos1)

    #FUNCIONES PARA AÑADIR INGRESO
    def añadirIngreso(self,pagos,ventas,productos,boton_fecha=False):
        #Crear la ventana emergente
        self.popUp_ingresos = tk.Toplevel()
        w,h = 300, 100
        util_ventana.centrarVentana(self.popUp_ingresos,w,h)
        #Crear el botón fecha
        if boton_fecha != False:
            fecha_ingreso = tk.Button(self.popUp_ingresos,text = "Fecha",command=lambda:self.mostrar_calendario(self.fecha_Label,pagos,ventas,actualizar=False))
            fecha_ingreso.grid(row = 4, column=1)
            string_fecha = gen.fecha_letras(datetime.date.today())
            self.fecha_Label = tk.Label(self.popUp_ingresos,text=string_fecha)
            self.fecha_Label.grid(row=4,column=2)
        #Labels con las instrucciones
        tk.Label(self.popUp_ingresos, text = "Cantidad:").grid(row = 0, column = 3)
        #Colocar la caja de texto para que el usuario ingrese la cantidad
        self.cajaTexto2 = tk.Entry(self.popUp_ingresos)
        self.cajaTexto2.grid(row = 1, column = 3)
        #Si no se han añadido productos, no pueden añadirse ventas
        if len(productos) < 1:
            gen.advertencia("Aún no se han añadido productos, por lo tanto aún no pueden añadirse ventas")
            self.popUp_ingresos.withdraw()
        else:
        #Botón para elegir un producto
            self.producto = tk.StringVar(self.popUp_ingresos,"Producto") #Asociar 
            menu = tk.OptionMenu(self.popUp_ingresos, self.producto, *productos["producto"]) 
            menu.grid(row=2, column = 1)
        #Botones aceptar y cancelar
            aceptar = tk.Button(self.popUp_ingresos, text = "Aceptar", command = lambda: self.aceptarIngreso(productos,ventas))
            aceptar.grid(row = 2, column = 2)
            cancelar = tk.Button(self.popUp_ingresos, text = "Cancelar", command = self.popUp_ingresos.withdraw)
            cancelar.grid(row= 4, column = 3)

        
    def aceptarIngreso(self,productos,ventas):
        #Recuperar el valor del menú
        producto = self.producto.get()
        try:
            #Guardar la cantidad en una variable como un entero
            cantidad = int(self.cajaTexto2.get())
        #Si la cantidad ingresada no es un número entero, mostrar error
        except TypeError:
            gen.advertencia("La cantidad debe ser un número entero. Por favor intente de nuevo", self.cajaTexto2)
        #Si no se eligió un producto, mostrar error:
        if producto == "Producto":
            gen.advertencia("Por favor seleccione un producto", self.cajaTexto2)
        #Agregar la venta al dataframe y csv de ventas
        else:
            indice = productos.index[productos["producto"]==producto] #Encontrar el índice del producto
            precio_producto = float(productos.iloc[indice,1]) #Obtener el precio del producto con el índice
            ingreso = cantidad*precio_producto
            try: 
                ventas.loc[len(ventas)] = [producto, cantidad, ingreso, self.fecha]
            except AttributeError:
                ventas.loc[len(ventas)] = [producto, cantidad, ingreso, datetime.date.today()]
            ventas.to_csv("ventas.csv")
            #Actualizar cuadro de ventas
            ventas1 = pd.read_csv("ventas.csv") # Se crea un df temporal para actualizar la tabla
            #Eliminar la columna inútil de index que tiene el csv >:v
            ventas1 = ventas1.drop(ventas1.iloc[:,0:1].columns, axis= 1)
            self.cuadro_ventasDiarias(ventas1) # Se llama a la función del cuadro para que vuelva a ser dibujada
            
            print(ventas1) #Print temporal para ver si funciona correctamente
            self.popUp_ingresos.withdraw()
        
      
    #FUNCIONES PARA AÑADIR PAGO
    def añadirPago(self,ventas,pagos,inversiones,recurrentes,boton_fecha=False):
        #Crear el popUP
        self.popUp_pagos = tk.Toplevel()
        self.popUp_pagos.title("Añadir un egreso") #Título
        #self.popUp_pagos.protocol("WM_DELETE_WINDOW", self.popUp_pagos.withdraw)
        w,h = 425, 150
        util_ventana.centrarVentana(self.popUp_pagos,w,h)
        self.marcar_Recurrente = tk.Button(self.popUp_pagos, text = "  ", width = 1, height = 1, command = lambda:gen.check(self.marcar_Recurrente))
        self.marcar_Inversion = tk.Button(self.popUp_pagos, text = "  ", width = 1, height = 1, command = lambda:gen.check(self.marcar_Inversion))
        self.popUp_pagos.config(width=w, height=h) #Dimensiones
        
        if boton_fecha != False:
            fecha_ingreso = tk.Button(self.popUp_pagos,text = "Fecha",command=lambda:self.mostrar_calendario(self.fecha_Label,pagos,ventas,actualizar=False))
            fecha_ingreso.grid(row = 4, column=1)
            string_fecha = gen.fecha_letras(datetime.date.today())
            fecha_Label = tk.Label(self.popUp_pagos,text=string_fecha)
            fecha_Label.grid(row=4,column=2)

        #Labels con las instrucciones
        tk.Label(self.popUp_pagos, text = "Nombre del pago").grid(row = 0, column = 1)
        tk.Label(self.popUp_pagos, text = "Monto del pago").grid(row = 0, column = 3)
        #Colocar cajas de texto para que el usuario ingrese los datos
        self.cajaTexto1 = tk.Entry(self.popUp_pagos)
        self.cajaTexto2 = tk.Entry(self.popUp_pagos)
        self.cajaTexto1.grid(row = 1, column = 1)
        self.cajaTexto2.grid(row = 1, column = 3)
        #Botones Marcar como recurrente y marcar como inversión
        tk.Label(self.popUp_pagos, text = "Marcar como recurrente").grid(row = 2, column = 2)
        tk.Label(self.popUp_pagos, text = "Marcar como inversión").grid(row = 3, column = 2)
        self.marcar_Recurrente.configure(text = "  ")
        self.marcar_Recurrente.grid(row=2,column=1)
        self.marcar_Inversion.configure(text = "  ")
        self.marcar_Inversion.grid(row=3,column=1)
        #Menu de Pagos Recurrentes
        if len(recurrentes) > 0:
            self.recurrente = tk.StringVar(self.popUp_pagos,"Pagos Recurrentes")
            menu = tk.OptionMenu(self.popUp_pagos, self.recurrente, *recurrentes["pago"],command = lambda x: self.pagoRecurrente(x,recurrentes)) 
            menu.grid(row=2, column = 3)
        #Botones aceptar y cancelar
        aceptar = tk.Button(self.popUp_pagos, text = "Aceptar", command = lambda: self.aceptarPago(pagos,recurrentes,inversiones))
        aceptar.grid(row = 3, column = 3)
        cancelar = tk.Button(self.popUp_pagos, text = "Cancelar", command = self.popUp_pagos.withdraw)
        cancelar.grid(row= 4, column = 3)
        
    def pagoRecurrente(self,x,recurrentes):
        self.cajaTexto1.insert(0,x)
        indice = recurrentes.index[recurrentes["pago"]==x]
        print(indice)
        self.cajaTexto2.insert(0,float(recurrentes.iloc[indice,1]))
        
    def aceptarPago(self,pagos,recurrentes,inversiones):
        try:
            #Nombre del pago
            pago = self.cajaTexto1.get()
            #Guardar el monto en una variable como un float con dos decimales
            monto = round(float(self.cajaTexto2.get()),2)
            #Si no se puso nombre al pago, mostrar error
            if pago == "":
                gen.advertencia("Por favor poner nombre al pago",self.cajaTexto1)
            #Agregar el pago al dataframe y csv de pagos, con su monto
            else:
                try:
                    pagos.loc[len(pagos)] = [pago, monto, fecha]
                except NameError:
                    pagos.loc[len(pagos)] = [pago, monto, datetime.date.today()]
                pagos.to_csv("pagos.csv")
                print(pagos) #Print temporal para ver si funciona correctamente
                self.popUp_pagos.withdraw()
        #Si el precio ingresado no es un número, mostrar error
        except TypeError:
            #Si el monto no es un número, mostrar error
            gen.advertencia("El monto ingresado no es válido. Por favor intente de nuevo", self.cajaTexto2)
        #Si se marcó el pago como recurrente, añadir a recurrentes 
        if self.marcar_Recurrente.cget("text") == "✓":
            #Si el nombre del pago ya está en recurrentes, mostrar error
            if pago in recurrentes.pago.values:
                gen.advertencia("Ya existe un pago recurrente con este nombre. Se ha añadido el pago, pero no se ha añadido a recurrentes")
            else:
                #Si no, añadir al dataframe y csv de recurrentes
                recurrentes.loc[len(recurrentes)] = [pago, monto]
                recurrentes.to_csv("recurrentes.csv")
            print(recurrentes) 
        #Si se marcó el pago como inversión, añadir a inversiones 
        if self.marcar_Inversion.cget("text") == "✓":
            try:
                inversiones.loc[len(inversiones)] = [pago, monto, fecha]
            except NameError:
                inversiones.loc[len(inversiones)] = [pago, monto, datetime.date.today()]
            inversiones.to_csv("inversiones.csv")
        pagos1 = pd.read_csv("pagos.csv")
        #Eliminar la columna inútil de index que tiene el csv >:v
        pagos1 = pagos1.drop(pagos1.iloc[:,0:1].columns, axis= 1)
        self.cuadro_pagosDiarios(pagos1)
        print(inversiones)    
            
 
    def controles_barra_superior(self, productos, ventas, pagos, recurrentes, inversiones):
        #self.fecha = datetime.date.today()
        #Botones de la contabilidad diaria
        self.boton_Fecha = tk.Button(self.barra_superior1, text = "Fecha:", command= lambda: self.mostrar_calendario(self.fecha_Label,pagos,ventas,actualizar=True))
        self.boton_Fecha.grid(row=0,column=0)
        try:
            string_fecha = gen.fecha_letras(self.fecha)
        except AttributeError:
            string_fecha = gen.fecha_letras(datetime.date.today())
        self.fecha_Label = tk.Label(self.barra_superior1,text=string_fecha)
        self.fecha_Label.grid(row=0,column=1)
        
        self.Añadir_Ingreso_Diario = tk. Button(self.barra_superior1, text="Añadir Ingreso",command= lambda: self.añadirIngreso(pagos,ventas,productos))
        self.Añadir_Ingreso_Diario.grid(row=1, column=0)
        self.Añadir_Pago_Diario = tk. Button(self.barra_superior1, text="Añadir Pago", command= lambda: self.añadirPago(ventas,pagos,inversiones,recurrentes))
        self.Añadir_Pago_Diario.grid(row=1, column=1)
        
    
    #creación de cuadro de ventas
    def cuadro_ventasDiarias(self, ventas):
        ventas["fecha"] = pd.to_datetime(ventas["fecha"])
        ventas["fecha"] = ventas["fecha"].dt.date
        try:
            self.cuadroVentas = ventas[ventas["fecha"]== self.fecha]
        except AttributeError:
            hoy = datetime.date.today()
            hoy = datetime.date(hoy.year,hoy.month,hoy.day)
            self.cuadroVentas = ventas[ventas["fecha"]== hoy]
        #se indica la tabla con los parametros en el siguente orden "frame donde se coloca, dataframe donde saca los datos, se quita la barra de opciones de la tabla, se muestra las opciones de visualización, se desactiva la función de edición"
        #### NOTA PARA MAR: ¡No toques los parametros que estan en False! No se como funcionan y no hay tiempo para usarlos
        self.tableVentas = Table(self.barra_media, dataframe= self.cuadroVentas, showtoolbar= False, showstatusbar= True, editable= False)
        self.tableVentas.show()
        self.tableVentas.redraw()
        
    def cuadro_pagosDiarios(self, pagos):
        pagos["fecha"] = pd.to_datetime(pagos["fecha"])
        pagos["fecha"] = pagos["fecha"].dt.date
        try:
            self.cuadroPagos = pagos[pagos["fecha"]== self.fecha]
        except AttributeError:
            hoy = datetime.date.today()
            hoy = datetime.date(hoy.year,hoy.month,hoy.day)
            self.cuadroPagos = pagos[pagos["fecha"]== hoy]
        #se indica la tabla con los parametros en el siguente orden "frame donde se coloca, dataframe donde saca los datos, se quita la barra de opciones de la tabla, se muestra las opciones de visualización, se desactiva la función de edición"
        #### NOTA PARA MAR: ¡No toques los parametros que estan en False! No se como funcionan y no hay tiempo para usarlos
        self.tablePagos = Table(self.barra_inferior, dataframe= self.cuadroPagos, showtoolbar= False, showstatusbar= True, editable= False)
        self.tablePagos.show()
        self.tablePagos.redraw()
