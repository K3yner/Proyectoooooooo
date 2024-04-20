import tkinter
import datetime
from tkcalendar import Calendar
import moduloGeneral as mG

#Crear ventana
ventana = tkinter.Tk()
#Dimensiones de la ventana
ventana.geometry("500x500")
#Etiqueta
etiqueta = tkinter.Label(ventana, text = "Hola Mundo")
#Posicionar etiqueta en medio hasta arriba
etiqueta.pack()
    #etiqueta.pack(side=tkinter.BOTTOM), .RIGHT, .LEFT


def saludo():
    print("Hola")
#Botón
boton = tkinter.Button(ventana, text = "Hola", command = saludo)
boton.pack()

def saludo_personalizado(nombre):
    print("Hola " + nombre)
    
boton2 = tkinter.Button(ventana, text = "Saludo", command = lambda: saludo_personalizado("Mar")) #Si la función tiene parámetros usar un lambda
boton2.pack()

#Caja de texto
cajaTexto = tkinter.Entry(ventana) #Se puede cambiar fuente y tipo de letra
cajaTexto.pack()
    #Recuperar texto de una caja
def textoDeLaCaja():
    texto = cajaTexto.get()   #Usar el método get
    print(texto)
    #Crear un botón que permita recuperar el texto de la caja
boton3 = tkinter.Button(ventana, text = "Imprimir", command = textoDeLaCaja)
boton3.pack()

    #Poner el texto de la caja en una etiqueta
def textoDeLaCaja():
    texto = cajaTexto.get()   #Usar el método get
    etiqueta["text"] = texto
boton3 = tkinter.Button(ventana, text = "Mostrar", command = textoDeLaCaja)
boton3.pack()

barra_menus = tkinter.Menu()
# Crear el primer menú.
menu_archivo = tkinter.Menu(barra_menus, tearoff=False)
# Agregarlo a la barra.
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
menu_archivo.add_command(label="Nuevo", command=lambda:print("Archivo"))
menu_archivo.add_command(label="Hola", command=lambda:print("Hola"))
menu_archivo.add_command(label="Adiós", command=lambda:print("Adiós"))
ventana.config(menu=barra_menus)



options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
value_inside = tkinter.StringVar(ventana)
value_inside.set("Select an Option")
question_menu = tkinter.OptionMenu(ventana, value_inside, *options_list) 
question_menu.pack()

entry = tkinter.Entry(ventana,width=50)
entry.pack()
entry.insert(0,"Hola mundo")

popUp = tkinter.Toplevel()
def check(boton):
    if boton.cget("text") == "  ":
        boton.configure(text = "✓")
        global check
        si = "si"
    else:
        boton.configure(text = "  ")
        si = "no"
    return si
        
boton = tkinter.Button(popUp,text=" ", command = lambda:check(boton))
boton.pack()
ver = tkinter.Button(popUp, text = "ver", command = lambda:ver(boton))
ver.pack()

def ver(boton):
    if boton.cget("text") == "  ":
        print("No")
    else:
        print("Sí")

hola = check(boton)
print(hola)

cal = Calendar(ventana, selectmode="day", showothermonthdays=False, showweeknumbers=False)
cal.pack()
cal._calendar.calevent_create(cal._canvas, "2020-01-01", "high", "", None)  # Selecciona el primer día del calendario
cal._calendar.calevent_create(cal._canvas, "2100-12-31", "high", "", None)

#CALENDARIO
"""def seleccionar_fecha(popUp):
    popUp.destroy()

# Crear calendario
cal = Calendar(hola, locale='es_ES', selectmode="day",maxdate=datetime.date.today())
cal.pack()

# Botón para seleccionar fecha
seleccionar = tkinter.Button(hola, text="Seleccionar Fecha", command=lambda:seleccionar_fecha(hola))
seleccionar.pack()

ver_fecha = tkinter.Button(ventana, text="Ver fecha",command=lambda:print(cal.get_date()))
ver_fecha.pack()"""


ventana.mainloop()