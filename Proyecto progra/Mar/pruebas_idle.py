Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter
... import datetime
... from tkcalendar import Calendar
... #Crear ventana
... ventana = tkinter.Tk()
... #Dimensiones de la ventana
... ventana.geometry("500x500")
... #Etiqueta
... etiqueta = tkinter.Label(ventana, text = "Hola Mundo")
... #Posicionar etiqueta en medio hasta arriba
... etiqueta.pack()
...     #etiqueta.pack(side=tkinter.BOTTOM), .RIGHT, .LEFT
... 
... 
... def saludo():
...     print("Hola")
... #Botón
... boton = tkinter.Button(ventana, text = "Hola", command = saludo)
... boton.pack()
... 
... def saludo_personalizado(nombre):
...     print("Hola " + nombre)
...     
... boton2 = tkinter.Button(ventana, text = "Saludo", command = lambda: saludo_personalizado("Mar")) #Si la función tiene parámetros usar un lambda
... boton2.pack()
... 
... #Caja de texto
... cajaTexto = tkinter.Entry(ventana) #Se puede cambiar fuente y tipo de letra
... cajaTexto.pack()
...     #Recuperar texto de una caja
... def textoDeLaCaja():
...     texto = cajaTexto.get()   #Usar el método get
...     print(texto)
...     #Crear un botón que permita recuperar el texto de la caja
... boton3 = tkinter.Button(ventana, text = "Imprimir", command = textoDeLaCaja)
... boton3.pack()
... 
...     #Poner el texto de la caja en una etiqueta
... def textoDeLaCaja():
...     texto = cajaTexto.get()   #Usar el método get
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


def check(boton):
    if boton.cget("text") == "  ":
        boton.configure(text = "✓")
        global check
        si = "si"
    else:
        boton.configure(text = "  ")
        si = "no"
    return si

popUp = tkinter.Toplevel(ventana)
        
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

def seleccionar_fecha():
    fecha_seleccionada = cal.get_date()
    etiqueta_fecha.config(text="Fecha seleccionada: " + fecha_seleccionada)

# Crear calendario
cal = Calendar(ventana, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack()

# Botón para seleccionar fecha
boton_seleccionar = tkinter.Button(ventana, text="Seleccionar Fecha", command=seleccionar_fecha)
boton_seleccionar.pack()

# Etiqueta para mostrar la fecha seleccionada
etiqueta_fecha = tkinter.Label(ventana, text="")
etiqueta_fecha.pack()






