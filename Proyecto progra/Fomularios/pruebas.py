import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

ventana = tk.Tk()
ventana.geometry("1000x1000")

df = pd.read_csv("productos.csv")

fig1 = Figure(figsize=(5,4),dpi=100)
fig1.add_subplot().bar(df['producto'], df['precio'])
canvas1 = FigureCanvasTkAgg(fig1, master=ventana)
canvas1.draw()
canvas1.get_tk_widget().grid(row=0,column=0)

categorías = pd.DataFrame(df.value_counts(df["categoría"])).reset_index()
fig2 = Figure(figsize=(5,4),dpi=100)
fig2.add_subplot().bar(categorías["categoría"],categorías["count"])
canvas2 = FigureCanvasTkAgg(fig2, master=ventana)
canvas2.draw()
canvas2.get_tk_widget().grid(row=0,column=1)


ventana.mainloop()

