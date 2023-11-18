import tkinter as tk

#Creando la ventana y sus dimensiones
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x300")

#Agregando el título
etiqueta = tk.Label(ventana, text="Calculadora")
etiqueta.grid(row=0, column=0, columnspan=3)

#Creando los botones, ajustando sus tamaños, dimensiones y separaciones
def opcion1():
    return 1

boton1 = tk.Button(ventana, text="1", command=opcion1,
                   width=5, height= 3)
boton1.grid(row=1, column=0, padx= 5, pady= 5)

def opcion2():
    return 2

boton2 = tk.Button(ventana, text="2", command=opcion2,
                   width=5, height= 3)
boton2.grid(row=1, column=1, padx= 5, pady= 5)

def opcion3():
    return 3

boton3 = tk.Button(ventana, text="3", command=opcion3,
                   width=5, height= 3)
boton3.grid(row=1, column=2, padx= 5, pady= 5)

def opcion4():
    return 4

boton4 = tk.Button(ventana, text="4", command=opcion4,
                   width=5, height= 3)
boton4.grid(row=2, column=0, padx= 5, pady= 5)

def opcion5():
    return 5

boton5 = tk.Button(ventana, text="5", command=opcion5,
                   width=5, height= 3)
boton5.grid(row=2, column=1, padx= 5, pady= 5)

def opcion6():
    return 6

boton6 = tk.Button(ventana, text="6", command=opcion6,
                   width=5, height= 3)
boton6.grid(row=2, column=2, padx= 5, pady= 5)

def opcion7():
    return 7

boton7 = tk.Button(ventana, text="7", command=opcion7,
                   width=5, height= 3)
boton7.grid(row=3, column=0, padx= 5, pady= 5)

def opcion8():
    return 8

boton8 = tk.Button(ventana, text="8", command=opcion8,
                   width=5, height= 3)
boton8.grid(row=3, column=1, padx= 5, pady= 5)

def opcion9():
    return 9

boton9 = tk.Button(ventana, text="9", command=opcion9,
                   width=5, height= 3)
boton9.grid(row=3, column=2, padx= 5, pady= 5)

def opcion0():
    return 0

boton0 = tk.Button(ventana, text="0", command=opcion0,
                   width=5, height= 3)
boton0.grid(row=4, column=0, padx= 5, pady= 5)

numero_actual = ""

def agregar_numero(numero):
    global numero_actual
    numero_actual += str(numero)

def calcular_resultado():
    global numero_actual
    resultado = eval(numero_actual)
    numero_actual = str(resultado)
    mostrar_resultado()

def mostrar_resultado():
    resultado_label.config(text=numero_actual)

# Botones de números
boton1 = tk.Button(ventana, text="1", command=lambda: agregar_numero(1))
boton1.grid(row=1, column=3)

# Botones de operaciones
boton_suma = tk.Button(ventana, text="+", command=lambda: agregar_numero("+"))
boton_suma.grid(row=2, column=3)

boton_resta = tk.Button(ventana, text="-", command=lambda: agregar_numero("-"))
boton_resta.grid(row=3, column=3)

boton_multiplicacion = tk.Button(ventana, text="*", command=lambda: agregar_numero("*"))
boton_multiplicacion.grid(row=4, column=3)

boton_division = tk.Button(ventana, text="/", command=lambda: agregar_numero("/"))
boton_division.grid(row=1, column=4)

# Botón de igual
boton_igual = tk.Button(ventana, text="=", command=calcular_resultado)
boton_igual.grid(row=2, column=4)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.grid(row=3, column=4, columnspan=3)
ventana.mainloop()