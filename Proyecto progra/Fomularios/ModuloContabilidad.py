import tkinter as tk
from Fomularios import ModuloGeneral as gen
import datetime
from tkcalendar import Calendar
import pandas as pd


#FUNCIONES PARA DEFINIR LA FECHA
def mostrar_calendario(fecha_Label):
     #Colocar el popUP
    calendario = tk.Toplevel()
    calendario.title("Seleccionar fecha") #Título
    #Crear calendario
    cal = Calendar(calendario,locale='es_ES', selectmode="day",maxdate=datetime.date.today())
    #Colocar calendario
    cal.pack()
    #Botón seleccionar fecha
    seleccionar = tk.Button(calendario, text="Seleccionar Fecha", command=lambda:seleccionar_fecha(calendario,cal,
    seleccionar,fecha_Label))
    seleccionar.pack()

def seleccionar_fecha(calendario,cal,seleccionar,fecha_Label="no"):
    global fecha
    fecha = cal.selection_get()
    string_fecha = gen.fecha_letras(fecha)
    if fecha_Label != "no":
        fecha_Label["text"] = string_fecha
    calendario.withdraw()
    seleccionar.destroy()

#FUNCIONES PARA AÑADIR INGRESO
def añadirIngreso(ventas,productos,boton_fecha=False):
    #Crear la ventana emergente
    popUp_ingresos = tk.Toplevel()
    #Crear el botón fecha
    if boton_fecha != False:
        fecha_ingreso = tk.Button(popUp_ingresos,text = "Fecha",command=lambda:mostrar_calendario(fecha_Label))
        fecha_ingreso.grid(row = 4, column=1)
        string_fecha = gen.fecha_letras(datetime.date.today())
        fecha_Label = tk.Label(popUp_ingresos,text=string_fecha)
        fecha_Label.grid(row=4,column=2)
    #Labels con las instrucciones
    tk.Label(popUp_ingresos, text = "Cantidad:").grid(row = 0, column = 3)
    #Colocar la caja de texto para que el usuario ingrese la cantidad
    cajaTexto2 = tk.Entry(popUp_ingresos)
    cajaTexto2.grid(row = 1, column = 3)
    #Si no se han añadido productos, no pueden añadirse ventas
    if len(productos) < 1:
        gen.advertencia("Aún no se han añadido productos, por lo tanto aún no pueden añadirse ventas")
        popUp_ingresos.withdraw()
    else:
    #Botón para elegir un producto
        global producto
        producto = tk.StringVar(popUp_ingresos,"Producto")
        #lista_productos = productos["producto"].tolist()
        menu = tk.OptionMenu(popUp_ingresos, producto, productos["producto"]) 
        menu.grid(row=2, column = 1)
    #Botones aceptar y cancelar
        aceptar = tk.Button(popUp_ingresos, text = "Aceptar", command = lambda: aceptarIngreso(popUp_ingresos,cajaTexto2,producto,productos,ventas))
        aceptar.grid(row = 2, column = 2)
        cancelar = tk.Button(popUp_ingresos, text = "Cancelar", command = popUp_ingresos.withdraw)
        cancelar.grid(row= 4, column = 3)

    
def aceptarIngreso(popUp_ingresos,cajaTexto2,producto,productos,ventas):
    #Recuperar el valor del menú
    producto = producto.get()
    try:
        #Guardar la cantidad en una variable como un entero
        cantidad = int(cajaTexto2.get())
        #Si no se eligió un producto, mostrar error:
        if producto == "Producto":
            gen.advertencia("Por favor seleccione un producto", cajaTexto2)
        #Agregar la venta al diccionario de ventas
        else:
            indice = productos.index[productos["producto"]==producto]
            precio_producto = float(productos.iloc[indice,1])
            ingreso = cantidad*precio_producto
            try: 
                ventas.loc[len(ventas)] = [producto, cantidad, ingreso, fecha]
                ventas.to_csv("ventas.csv")
            except NameError:
                ventas.loc[len(ventas)] = [producto, cantidad, ingreso, datetime.date.today()]
                ventas.to_csv("ventas.csv")
            print(ventas) #Print temporal para ver si funciona correctamente
            popUp_ingresos.withdraw()
        #Si la cantidad ingresada no es un número entero, mostrar error
    except TypeError:
        gen.advertencia("La cantidad debe ser un número entero. Por favor intente de nuevo", cajaTexto2)

        
#FUNCIONES PARA AÑADIR PAGO
def añadirPago(pagos,inversiones,recurrentes,boton_fecha=False):
    #Crear el popUP
    popUp_pagos = tk.Toplevel()
    popUp_pagos.title("Añadir un egreso") #Título
    popUp_pagos.protocol("WM_DELETE_WINDOW", popUp_pagos.withdraw)
    marcar_Recurrente = tk.Button(popUp_pagos, text = "  ", width = 1, height = 1, command = lambda:gen.check(marcar_Recurrente))
    marcar_Inversion = tk.Button(popUp_pagos, text = "  ", width = 1, height = 1, command = lambda:gen.check(marcar_Inversion))
    popUp_pagos.config(width=500, height=200) #Dimensiones
    
    if boton_fecha != False:
        fecha_ingreso = tk.Button(popUp_pagos,text = "Fecha",command=lambda:mostrar_calendario(fecha_Label))
        fecha_ingreso.grid(row = 4, column=1)
        string_fecha = gen.fecha_letras(datetime.date.today())
        fecha_Label = tk.Label(popUp_pagos,text=string_fecha)
        fecha_Label.grid(row=4,column=2)

    #Labels con las instrucciones
    tk.Label(popUp_pagos, text = "Nombre del pago").grid(row = 0, column = 1)
    tk.Label(popUp_pagos, text = "Monto del pago").grid(row = 0, column = 3)
    #Colocar cajas de texto para que el usuario ingrese los datos
    cajaTexto1 = tk.Entry(popUp_pagos)
    cajaTexto2 = tk.Entry(popUp_pagos)
    cajaTexto1.grid(row = 1, column = 1)
    cajaTexto2.grid(row = 1, column = 3)
    #Botones Marcar como recurrente y marcar como inversión
    tk.Label(popUp_pagos, text = "Marcar como recurrente").grid(row = 2, column = 2)
    tk.Label(popUp_pagos, text = "Marcar como inversión").grid(row = 3, column = 2)
    marcar_Recurrente.configure(text = "  ")
    marcar_Recurrente.grid(row=2,column=1)
    marcar_Inversion.configure(text = "  ")
    marcar_Inversion.grid(row=3,column=1)
    #Menu de Pagos Recurrentes
    if len(recurrentes) > 0:
        global recurrente
        recurrente = tk.StringVar(popUp_pagos,"Pagos Recurrentes")
        menu = tk.OptionMenu(popUp_pagos, recurrente, *recurrentes["pago"],command = lambda x: pagoRecurrente(x,cajaTexto1,cajaTexto2,recurrentes)) 
        menu.grid(row=2, column = 3)
    #Botones aceptar y cancelar
    aceptar = tk.Button(popUp_pagos, text = "Aceptar", command = lambda: aceptarPago(popUp_pagos,cajaTexto1,cajaTexto2,pagos,marcar_Recurrente,marcar_Inversion,recurrentes,inversiones))
    aceptar.grid(row = 3, column = 3)
    cancelar = tk.Button(popUp_pagos, text = "Cancelar", command = popUp_pagos.withdraw)
    cancelar.grid(row= 4, column = 3)
    
def pagoRecurrente(recurrente,cajaTexto1,cajaTexto2,recurrentes):
    cajaTexto1.insert(0,recurrente)
    indice = recurrentes.index[recurrentes["pago"]==recurrente]
    cajaTexto2.insert(0,float(recurrentes.iloc[indice,1]))
    
def aceptarPago(popUp_pagos,cajaTexto1,cajaTexto2,pagos,marcar_Recurrente,marcar_Inversion,recurrentes,inversiones):
    try:
        #Nombre del pago
        pago = cajaTexto1.get()
        #Guardar el monto en una variable como un float con dos decimales
        monto = round(float(cajaTexto2.get()),2)
        #Si no se puso nombre al pago, mostrar error
        if pago == "":
            gen.advertencia("Por favor poner nombre al pago",cajaTexto1)
        #Agregar el pago al diccionario de pagos, con su monto
        else:
            try:
                pagos.loc[len(pagos)] = [pago, monto, fecha]
            except NameError:
                pagos.loc[len(pagos)] = [pago, monto, datetime.date.today()]
            pagos.to_csv("pagos.csv")
            print(pagos) #Print temporal para ver si funciona correctamente
            popUp_pagos.withdraw()
    #Si el precio ingresado no es un número, mostrar error
    except TypeError:
        #Si el monto no es un número, mostrar error
        gen.advertencia("El monto ingresado no es válido. Por favor intente de nuevo", cajaTexto2)
    #Si se marcó el pago como recurrente, añadir a recurrentes 
    if marcar_Recurrente.cget("text") == "✓":
        #Si el nombre del pago ya está en recurrentes, mostrar error
        if pago in recurrentes.pago.values:
            gen.advertencia("Ya existe un pago recurrente con este nombre. Se ha añadido el pago, pero no se ha añadido a recurrentes")
        else:
            recurrentes.loc[len(recurrentes)] = [pago, monto]
            recurrentes.to_csv("recurrentes.csv")
        print(recurrentes) 
    #Si se marcó el pago como inversión, añadir a inversiones 
    if marcar_Inversion.cget("text") == "✓":
        try:
            inversiones.loc[len(inversiones)] = [pago, monto, fecha]
        except NameError:
            inversiones.loc[len(inversiones)] = [pago, monto, datetime.date.today()]
        inversiones.to_csv("inversiones.csv")
    print(inversiones)

    
#CONTA MENSUAL
def mes():
    print(datetime.date.today()) #TEMPORAL
     