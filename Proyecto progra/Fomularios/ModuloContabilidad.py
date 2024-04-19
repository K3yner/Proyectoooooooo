import tkinter as tk
from Fomularios import ModuloGeneral as gen
import datetime
from tkcalendar import Calendar

ventas = []
pagos = []
recurrentes = {}
inversiones = []

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
def añadirIngreso(ventas,productos):
    popUp_ingresos = tk.Toplevel()
    popUp_ingresos.withdraw()
    popUp_ingresos.title("Añadir un ingreso") #Título
    popUp_ingresos.protocol("WM_DELETE_WINDOW", popUp_ingresos.withdraw)
    # Botón Fecha
    fecha = datetime.date.today()
    #Colocar el popUP
    calendario = tk.Toplevel()
    calendario.title("Seleccionar fecha") #Título
    #Ocultar popUp
    calendario.withdraw()
    #Crear calendario
    cal = Calendar(calendario,locale='es_ES', selectmode="day",maxdate=datetime.date.today())
    popUp_ingresos.config(width=500, height=200) #Dimensiones
    popUp_ingresos.deiconify()
    #Labels con las instrucciones
    tk.Label(popUp_ingresos, text = "Cantidad:").grid(row = 0, column = 3)
    #Colocar la caja de texto para que el usuario ingrese la cantidad
    cajaTexto2 = tk.Entry(popUp_ingresos)
    cajaTexto2.grid(row = 1, column = 3)
    #Lista de productos
    nombres_productos = [] 
    for x in productos:
        for y in productos[x]:
            nombres_productos.append(y)
    #Si no se han añadido productos, no pueden añadirse ventas
    if nombres_productos == []:
        gen.advertencia("Aún no se han añadido productos, por lo tanto aún no pueden añadirse ventas")
        popUp_ingresos.withdraw()
    else:
    #Botón para elegir un producto
        global producto
        producto = tk.StringVar(popUp_ingresos,"Producto")
        menu = tk.OptionMenu(popUp_ingresos, producto, *nombres_productos) 
        menu.grid(row=2, column = 1)
    #Botones aceptar y cancelar
        aceptar = tk.Button(popUp_ingresos, text = "Aceptar", command = lambda: aceptarIngreso(popUp_ingresos,cajaTexto2,producto,productos,ventas,nombres_productos))
        aceptar.grid(row = 2, column = 2)
        cancelar = tk.Button(popUp_ingresos, text = "Cancelar", command = popUp_ingresos.withdraw)
        cancelar.grid(row= 4, column = 3)
    
def aceptarIngreso(popUp_ingresos,cajaTexto2,producto,productos,ventas,nombres_productos):
    #Lista de los precios de los productos
    precios_productos = []
    for x in productos:
        for y in productos[x]:
            precios_productos.append(productos[x][y])
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
            ingreso = cantidad*precios_productos[nombres_productos.index(producto)]
            ventas.append([producto, cantidad, ingreso, fecha])
            print(ventas) #Print temporal para ver si funciona correctamente
            popUp_ingresos.withdraw()
        #Si la cantidad ingresada no es un número entero, mostrar error
    except:
        gen.advertencia("La cantidad debe ser un número entero. Por favor intente de nuevo", cajaTexto2)

        
#FUNCIONES PARA AÑADIR PAGO
def añadirPago(inversiones,fecha):

    cal = Calendar(locale='es_ES', selectmode="day",maxdate=datetime.date.today())
    #Colocar el popUP
    popUp_pagos = tk.Toplevel()
    popUp_pagos.title("Añadir un egreso") #Título
    popUp_pagos.protocol("WM_DELETE_WINDOW", popUp_pagos.withdraw)
    popUp_pagos.withdraw()
    marcar_Recurrente = tk.Button(popUp_pagos, text = "  ", width = 1, height = 1, command = lambda:gen.check(marcar_Recurrente))
    marcar_Inversion = tk.Button(popUp_pagos, text = "  ", width = 1, height = 1, command = lambda:gen.check(marcar_Inversion))
    popUp_pagos.deiconify()
    popUp_pagos.config(width=500, height=200) #Dimensiones
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
    if recurrentes != {}:
        global recurrente
        recurrente = tk.StringVar(popUp_pagos,"Pagos Recurrentes")
        menu = tk.OptionMenu(popUp_pagos, recurrente, *recurrentes.keys(),command = lambda x: pagoRecurrente(x,cajaTexto1,cajaTexto2,recurrentes)) 
        menu.grid(row=2, column = 3)
    #Botones aceptar y cancelar
    aceptar = tk.Button(popUp_pagos, text = "Aceptar", command = lambda: aceptarPago(popUp_pagos,cajaTexto1,cajaTexto2,pagos,marcar_Recurrente,marcar_Inversion,recurrentes,inversiones))
    aceptar.grid(row = 3, column = 3)
    cancelar = tk.Button(popUp_pagos, text = "Cancelar", command = popUp_pagos.withdraw)
    cancelar.grid(row= 4, column = 3)
    
def pagoRecurrente(recurrente,cajaTexto1,cajaTexto2,recurrentes):
    cajaTexto1.insert(0,recurrente)
    cajaTexto2.insert(0,recurrentes[recurrente])
    
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
            pagos.append([pago,monto,fecha])
            print(pagos) #Print temporal para ver si funciona correctamente
            popUp_pagos.withdraw()
            #Si el precio ingresado no es un número, mostrar error
    except:
        #Si el monto no es un número, mostrar error
        gen.advertencia("El monto ingresado no es válido. Por favor intente de nuevo", cajaTexto2)
    #Si se marcó el pago como recurrente, añadir a recurrentes (NO FUNCIONAL)
    if marcar_Recurrente.cget("text") == "✓":
        error = False #Variable de control de errores
        #Si el nombre del pago ya está en recurrentes, mostrar error
        for x in recurrentes:
            if x == pago:
                error = True 
                gen.advertencia("Ya existe un pago recurrente con este nombre. Se ha añadido el pago, pero no se ha añadido a recurrentes")
        if error == False:
            recurrentes[pago] = monto
        print(recurrentes) 
    #Si se marcó el pago como inversión, añadir a inversiones (NO FUNCIONAL)
    if marcar_Inversion.cget("text") == "✓":
        inversiones.append([pago,monto,fecha])
    print(inversiones)

    
#CONTA MENSUAL
def mes():
    print(datetime.date.today()) #TEMPORAL

def añadirPago_mensual(popUp_pagos,recurrentes,pagos,marcar_Recurrente,marcar_Inversion,inversiones,calendario):
    añadirPago(popUp_pagos,recurrentes,pagos,marcar_Recurrente,marcar_Inversion,inversiones)
    fecha_pago = tk.Button(popUp_pagos,text = "Fecha",command=lambda:mostrar_calendario(fecha_Label,calendario,))
    fecha_pago.grid(row = 4, column=1)
    string_fecha = gen.fecha_letras(datetime.date.today())
    fecha_Label = tk.Label(popUp_pagos,text=string_fecha)
    fecha_Label.grid(row=4,column=2)
    
def añadirIngreso_mensual(ventas,productos,popUp_ingresos):
    añadirIngreso(ventas,productos,popUp_ingresos,)
    fecha_pago = tk.Button(popUp_ingresos,text = "Fecha",command=lambda:mostrar_calendario(fecha_Label,calendario))
    fecha_pago.grid(row = 4, column=1)
    string_fecha = gen.fecha_letras(datetime.date.today())
    fecha_Label = tk.Label(popUp_ingresos,text=string_fecha)
    fecha_Label.grid(row=4,column=2)