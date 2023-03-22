import tkinter as tk
from tkinter import ttk

# Valores de cambio de moneda
cambio = {
    'USD': {'MXN': 18.24, 'EUR': 0.92},
    'MXN': {'USD': 0.053, 'EUR': 0.049},
    'EUR': {'USD': 1.07, 'MXN': 20.02}
}

# Función para realizar el cálculo de conversión
def convertir():
    moneda_origen = lista_origen.get()
    moneda_destino = lista_destino.get()
    cantidad = float(entrada_cantidad.get())
    resultado = cantidad * cambio[moneda_origen][moneda_destino]
    etiqueta_resultado.config(text=f"{cantidad} {moneda_origen} = {resultado:.2f} {moneda_destino}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Monedas")

# Crear los widgets de la interfaz
etiqueta_cantidad = tk.Label(ventana, text="Cantidad:")
entrada_cantidad = tk.Entry(ventana)
etiqueta_origen = tk.Label(ventana, text="Moneda de origen:")
lista_origen = ttk.Combobox(ventana, values=["USD", "MXN", "EUR"])
lista_origen.current(0)
etiqueta_destino = tk.Label(ventana, text="Moneda de destino:")
lista_destino = ttk.Combobox(ventana, values=["USD", "MXN", "EUR"])
lista_destino.current(0)
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
etiqueta_resultado = tk.Label(ventana, text="")

# Alinear los widgets en la ventana
etiqueta_cantidad.grid(row=0, column=0)
entrada_cantidad.grid(row=0, column=1)
etiqueta_origen.grid(row=1, column=0)
lista_origen.grid(row=1, column=1)
etiqueta_destino.grid(row=2, column=0)
lista_destino.grid(row=2, column=1)
boton_convertir.grid(row=3, column=1)
etiqueta_resultado.grid(row=4, column=0, columnspan=2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()

