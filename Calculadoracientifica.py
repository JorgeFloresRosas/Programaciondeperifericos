from tkinter import *

import math
ventana = Tk()
ventana.title('Calculadora')
i = 0
e_texto = Entry(ventana, font = ('Calibri 20'))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
# Función para reducir
def reducir():
    global i
    i -= 1
    e_texto.delete(i, END)
# Función para borrar
def borrar():
    e_texto.delete(0, END)
    i = 0
# Función para calcular
def operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0
# Función para convertir un número a notación científica
def convertir_notacion_cientifica():
    try:
        numero = float(e_texto.get())
        notacion_cientifica = "{:e}".format(numero)
        e_texto.delete(0, END)  # Borra el contenido de la entrada
        e_texto.insert(END, notacion_cientifica)
    except ValueError:
        resultado.config(text="Error: Ingresa un número válido.")
#texto para raiz
entrada_n = Entry(ventana, width=5)
entrada_n.grid(row=0, column=4, columnspan= 4)
#raiz n
def calcular_raiz_n():
    try:
        numero = float(e_texto.get())
        n = float(entrada_n.get())
        resultado = numero ** (1/n)
        e_texto.delete(0, END)  # Borra el contenido de la entrada
        e_texto.insert(END, resultado)
    except ValueError:
        resultado.config(text="Error: Ingresa un número válido.")
    except ZeroDivisionError:
        resultado.config(text="Error: n no puede ser cero.")
#Funcion raíz
def calcular_raiz_cuadrada():
    try:
        numero = float(e_texto.get())
        resultado = math.sqrt(numero)
        e_texto.delete(0, END)  # Borra el contenido de la entrada
        e_texto.insert(END, resultado)
    except ValueError:
        resultado_label.config(text="Error: Ingresa un número válido.")
# Función para modificar estado
def SwitchButtonState():
    if (botonswitch['text']=='ON'):
        botonswitch['text']= 'OFF'
    else:
        botonswitch['text']='ON'
    
    if (boton1['state']==NORMAL):
        boton1['state']=DISABLED
    else:
        boton1['state']=NORMAL
        
    if (boton2['state']==NORMAL):
        boton2['state']=DISABLED
    else:
        boton2['state']=NORMAL
    
    if (boton3['state']==NORMAL):
        boton3['state']=DISABLED
    else:
        boton3['state']=NORMAL
    
    if (boton4['state']==NORMAL):
        boton4['state']=DISABLED
    else:
        boton4['state']=NORMAL
# Variable para rastrear el estado del número (positivo o negativo)
numero_negativo = False
# Funcion Cambiar signo
def cambiar_signo():
    global numero_negativo
    numero = e_texto.get()
    if numero and numero != '0':
        if numero_negativo:
            e_texto.delete(0, END)
            e_texto.insert(0, numero[1:])
        else:
            e_texto.delete(0, END)
            e_texto.insert(0, '-' + numero)
        numero_negativo = not numero_negativo
#Calcular porcentaje
def calcular_porcentaje():
    try:
        numero = float(e_texto.get())
        resultado = numero / 100
        e_texto.delete(0, END)  # Borra el contenido de la entrada
        e_texto.insert(END, resultado)
    except ValueError:
        resultado.config(text="Error: Ingresa un número válido.")
botonsigno = Button(ventana, text = '+/-', width = 5, heigh =2, command = lambda: cambiar_signo())
botonexp = Button(ventana, background='blue', text = 'e', width = 5, heigh =2, command = lambda: convertir_notacion_cientifica())
boton1 = Button(ventana, borderwidth= 5, text = '1', width = 5, height = 2,state= DISABLED, command = lambda: click_boton(1))
boton2 = Button(ventana, font='arial', text = '2', width = 5, height = 2,state= DISABLED, command = lambda: click_boton(2))
boton3 = Button(ventana, foreground='red', text = '3', width = 5, height = 2,state= DISABLED, command = lambda: click_boton(3))
boton4 = Button(ventana, background='purple1', text = '4', width = 5, height = 2,state= DISABLED, command = lambda: click_boton(4))
boton5 = Button(ventana, borderwidth=10, text = '5', width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, foreground='orange', text = '6', width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = '7', width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = '8', width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = '9', width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = '0', width = 16, height = 2, command = lambda: click_boton(0))
botonAC = Button(ventana, text = 'AC', width = 5, height = 2, command = lambda: borrar())
botonpar1 = Button(ventana, text = '(', width = 5, height = 2, command = lambda: click_boton('('))
botonpar2 = Button(ventana, text = ')', width = 5, height = 2, command = lambda: click_boton(')'))
botonpunto = Button(ventana, text = '.', width = 5, height = 2, command = lambda: click_boton('.'))
botondiv = Button(ventana, text = '/', width = 5, height = 2, command = lambda: click_boton('/'))
botonmul = Button(ventana, text = '*', width = 5, height = 2, command = lambda: click_boton('*'))
botonres = Button(ventana, text = '-', width = 5, height = 2, command = lambda: click_boton('-'))
botonsum = Button(ventana, text = '+', width = 5, height = 2, command = lambda: click_boton('+'))
botonigual = Button(ventana, text = '=', width = 5, height = 2, command = lambda: operacion())
botonreducir = Button(ventana, text = '<-', width = 5, height = 2, command = lambda: reducir())
botonswitch = Button(ventana, text = 'ON', width = 5, height = 2, command = lambda: SwitchButtonState())
botonraiz = Button(ventana, text = '√', width = 5, height = 2, command = lambda: calcular_raiz_cuadrada())
botonraizn = Button(ventana, text = 'n√', width = 5, height = 2, command = lambda: calcular_raiz_n())
botonporcentaje = Button(ventana, text = '%', width = 5, height = 2, command = lambda: calcular_porcentaje())
botonporcentaje.grid(row = 7, column = 2, padx = 5, pady = 5)
boton1.grid(row = 5, column = 0, padx = 5, pady = 5)
boton2.grid(row = 5, column = 1, padx = 5, pady = 5)
boton3.grid(row = 5, column = 2, padx = 5, pady = 5)
boton4.grid(row = 4, column = 0, padx = 5, pady = 5)
boton5.grid(row = 4, column = 1, padx = 5, pady = 5)
boton6.grid(row = 4, column = 2, padx = 5, pady = 5)
boton7.grid(row = 3, column = 0, padx = 5, pady = 5)
boton8.grid(row = 3, column = 1, padx = 5, pady = 5)
boton9.grid(row = 3, column = 2, padx = 5, pady = 5)
boton0.grid(row = 6, column = 0, columnspan = 2, padx = 5, pady = 5)
botonAC.grid(row = 1, column = 0, padx = 5, pady = 5)
botonpar1.grid(row = 2, column = 1, padx = 5, pady = 5)
botonpar2.grid(row = 2, column = 2, padx = 5, pady = 5)
botonpunto.grid(row = 6, column = 2, padx = 5, pady = 5)
botondiv.grid(row = 2, column = 3, padx = 5, pady = 5)
botonmul.grid(row = 3, column = 3, padx = 5, pady = 5)
botonres.grid(row = 4, column = 3, padx = 5, pady = 5)
botonsum.grid(row = 5, column = 3, padx = 5, pady = 5)
botonigual.grid(row = 6, column = 3, padx = 5, pady = 5)
botonexp.grid(row = 1, column = 2, padx = 5, pady = 5)
botonreducir.grid(row = 1, column = 1, padx = 5, pady = 5)
botonswitch.grid(row = 1, column = 3, padx = 5, pady = 5)
botonsigno.grid(row = 2, column = 0, padx = 5, pady = 5)
botonraiz.grid(row = 7, column = 0, padx = 5, pady = 5)
botonraizn.grid(row = 7, column = 1, padx = 5, pady = 5)

ventana.mainloop()