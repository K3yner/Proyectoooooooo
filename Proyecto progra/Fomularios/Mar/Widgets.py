import tkinter as tk
import datetime
from tkcalendar import Calendar
import moduloProductos as pr
import moduloContabilidad as cnt
import moduloGeneral as gen

#Ventanas temporales para los widgets.
pagina12 = tk.Tk()
pagina12.title("Productos")
pagina12.grid()
pagina12.geometry("500x500")

pagina1 = tk.Tk()
pagina1.title("Contabilidad diaria")
pagina1.grid()
pagina1.geometry("500x500")

#PRODUCTOS
#Crear diccionario de productos vacíos
productos = {"Sin categoría":{}}

#Botón Añadir categoría
Añadir_Categoria = tk. Button(pagina12, text="Añadir Categoría", command= lambda: pr.añadirCategoria(productos))
Añadir_Categoria.grid(row=2, column=1)

#Botón Añadir producto
Añadir_Producto = tk.Button(pagina12, text="Añadir Producto", command = lambda: pr.añadirProducto(productos))
Añadir_Producto.grid(row=2, column=2)

#Buscador
buscador_productos = tk.Entry(pagina12,width=50)
buscador_productos.grid(row=0,column=2)
buscador_productos.insert(0,"🔎                       Buscar un producto")
buscador_productos.bind("<FocusIn>", lambda x:gen.borrar_texto(x,buscador_productos))
buscador_productos.bind("<FocusOut>", lambda x:pr.texto_buscador_productos(x,buscador_productos))
buscador_productos.bind("<Return>", lambda x:pr.buscar_producto(x,buscador_productos,productos,pagina12))

#CONTABILIDAD
#Estructuras de datos
ventas = []
pagos = []
recurrentes = {}
inversiones = {}

#Colocar el popUP
popUp_pagos = tk.Toplevel()
popUp_pagos.title("Añadir un egreso") #Título
popUp_pagos.protocol("WM_DELETE_WINDOW", popUp_pagos.withdraw)
popUp_pagos.withdraw()
marcar_Recurrente = tk.Button(popUp_pagos, text = "  ", width = 1, height = 1, command = lambda:gen.check(marcar_Recurrente))
marcar_Inversion = tk.Button(popUp_pagos, text = "  ", width = 1, height = 1, command = lambda:gen.check(marcar_Inversion))

#Colocar el popUP
popUp_ingresos = tk.Toplevel()
popUp_ingresos.title("Añadir un ingreso") #Título
popUp_ingresos.protocol("WM_DELETE_WINDOW", popUp_ingresos.withdraw)
popUp_ingresos.withdraw()

#Botón Fecha
fecha = datetime.date.today()
#Colocar el popUP
calendario = tk.Toplevel()
calendario.title("Seleccionar fecha") #Título
#Ocultar popUp
calendario.withdraw()
#Crear calendario
cal = Calendar(calendario,locale='es_ES', selectmode="day",maxdate=datetime.date.today())
#Set fecha incial
string_fecha = gen.fecha_letras(fecha)
boton_Fecha = tk.Button(pagina1, text = "Fecha:", command=lambda:cnt.mostrar_calendario(fecha_Label,calendario,cal))
boton_Fecha.grid(row=0,column=0)
fecha_Label = tk.Label(pagina1,text=string_fecha)
fecha_Label.grid(row=0,column=1)

#DIARIA
#Botón Añadir ingreso
Añadir_Ingreso_Diario = tk. Button(pagina1, text="Añadir Ingreso", command= lambda: cnt.añadirIngreso(ventas,cal,productos,popUp_ingresos))
Añadir_Ingreso_Diario.grid(row=2, column=1)

#Botón Añadir pago
Añadir_Pago_Diario = tk. Button(pagina1, text="Añadir Pago", command= lambda: cnt.añadirPago(popUp_pagos,recurrentes,pagos,marcar_Recurrente,marcar_Inversion,cal,inversiones))
Añadir_Pago_Diario.grid(row=2, column=2)

#MENSUAL
def cambiarA_diario():
    #Por ahora estoy borrando los botones, pero en la estructura mejor
    #creemos subventanas para diario y mensual
    Añadir_Pago_Mensual.grid_forget()
    Añadir_Ingreso_Mensual.grid_forget()
    boton_Mes.grid_forget()
    conta_diaria.grid_forget()
    Añadir_Ingreso_Diario.grid(row=2, column=1)
    Añadir_Pago_Diario.grid(row=2, column=2)
    boton_Fecha.grid(row=0,column=0)
    fecha_Label["text"] = gen.fecha_letras(datetime.date.today())
    conta_mensual.grid(row=8, column = 2)

Añadir_Ingreso_Mensual = tk. Button(pagina1, text="Añadir Ingreso", command= lambda: cnt.añadirIngreso_mensual(ventas,cal,productos,popUp_ingresos))
Añadir_Pago_Mensual = tk. Button(pagina1, text="Añadir Pago", command= lambda: cnt.añadirPago_mensual(popUp_pagos,recurrentes,pagos,marcar_Recurrente,marcar_Inversion,cal,inversiones,calendario))
boton_Mes = tk.Button(pagina1, text="Mes: ", command = cnt.mes)
conta_diaria = tk.Button(pagina1, text="Diario", command = cambiarA_diario)

#Botón "Mensual
def cambiarA_mensual():
    #Por ahora estoy borrando y recolocando los botones, pero en la estructura mejor
    #creemos subventanas para diario y mensual
    Añadir_Ingreso_Diario.grid_forget()
    Añadir_Pago_Diario.grid_forget()
    boton_Fecha.grid_forget()
    conta_mensual.grid_forget()
    Añadir_Pago_Mensual.grid(row=2, column=3)
    Añadir_Ingreso_Mensual.grid(row=2, column=2)
    boton_Mes.grid(row = 0, column = 0)
    fecha_Label["text"] = "Abril"  #Temporal
    conta_diaria.grid(row = 8, column = 2)
    
conta_mensual = tk.Button(pagina1,text="Mensual",command = cambiarA_mensual)
conta_mensual.grid(row=8, column = 2)


pagina12.mainloop()
pagina1.mainloop()


