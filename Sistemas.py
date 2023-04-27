import tkinter as tk

# Crea una ventana
ventana = tk.Tk()
ventana.geometry("300x200") # Establece las dimensiones de la ventana

# Crea un campo de texto
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.pack() # Añade el campo de texto a la ventana

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack() # Añade la entrada a la ventana

# Crea un botón de enviar
def enviar():
    print("El nombre es:", entrada_nombre.get())

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)
boton_enviar.pack() # Añade el botón a la ventana

# Inicia el bucle principal de la ventana
ventana.mainloop()
