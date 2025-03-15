import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar():
    info = entry.get()
    if info != "":
        lista_box.insert(tk.END, info)  # Inserta la información en la lista
        entry.delete(0, tk.END)  # Borra el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese algo en el campo de texto.")

# Función para limpiar la lista y el campo de texto
def limpiar():
    entry.delete(0, tk.END)  # Borra el campo de texto
    lista_box.delete(0, tk.END)  # Borra la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de GUI para Datos")

# Etiqueta para el título
etiqueta = tk.Label(ventana, text="Ingrese Información:")
etiqueta.pack(pady=10)

# Campo de texto para ingresar información
entry = tk.Entry(ventana, width=40)
entry.pack(pady=10)

# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

# Lista para mostrar la información agregada
lista_box = tk.Listbox(ventana, width=50, height=10)
lista_box.pack(pady=10)

# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()
