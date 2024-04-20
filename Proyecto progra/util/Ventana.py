def centrarVentana(ventana, aplicación_ancho,aplicación_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2)-(aplicación_ancho/2))
    y = int((pantalla_largo/2)-(aplicación_largo/2))
    return ventana.geometry(f"{aplicación_ancho}x{aplicación_largo}+{x}+{y}")