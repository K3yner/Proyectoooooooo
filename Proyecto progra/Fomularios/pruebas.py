import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x500")

cuadro = ttk.Treeview(ventana, columns=("col1", "col2", "col3"))
w = 80
columnas =["#0","col1", "col2", "col3"]
for i in range(0,len(columnas)-1):
    cuadro.column(columnas[i], width=w, anchor="center")
nombres_columnas = ["Ventas", "Pagos", "Ingresos", "Egresos"]
for i in range(0,len(columnas)-1):
    cuadro.heading(columnas[i], text= nombres_columnas[i], anchor= "center")

ventana.mainloop()

