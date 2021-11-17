import tkinter as tk
raiz = tk.Tk()
frame1 = tk.Frame(raiz)
frame1.pack()

operacion = ''
resultado = 0

# --------------------pantalla--------------------------
numeroPantalla = tk.StringVar()
pantalla = tk.Entry(frame1, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)  # pad para separar del borde
pantalla.config(background='black', fg='#03f943', justify='right')

# ------------------botonespulsados---------------------

def numeroPulsado(num):
    global operacion
    if operacion != '':
        numeroPantalla.set(num)
        operacion = ''
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

def suma(num):
    global operacion  
    global resultado
    resultado += int(num)
    operacion = 'suma'
    numeroPantalla.set(resultado)

def resta(num):
    global operacion  
    global resultado
    resultado -= int(num)
    operacion = 'resta'
    numeroPantalla.set(resultado)

def multiplicar(num):
    global operacion
    global resultado
    resultado *= int(num)
    operacion = 'multiplicacion'
    numeroPantalla.set(resultado)

def division(num):
    global operacion
    global resultado
    resultado /= int(num)
    operacion = 'division'
    numeroPantalla.set(resultado)
# ------------------funcion el resultado---------------------

def el_resultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado = 0

# ------------------fila1-------------------------------

boton7 = tk.Button(frame1, text='7', width='3', command=lambda: numeroPulsado('7'))
boton8 = tk.Button(frame1, text='8', width='3', command=lambda: numeroPulsado('8'))
boton9 = tk.Button(frame1, text='9', width='3', command=lambda: numeroPulsado('9'))
botondiv = tk.Button(frame1, text='/', width='3', command=lambda: division(numeroPantalla.get()))
boton7.grid(row=2, column=1)
boton8.grid(row=2, column=2)
boton9.grid(row=2, column=3)
botondiv.grid(row=2, column=4)
# ------------------fila2-------------------------------
boton4 = tk.Button(frame1, text='4', width='3', command=lambda: numeroPulsado('4'))
boton5 = tk.Button(frame1, text='5', width='3', command=lambda: numeroPulsado('5'))
boton6 = tk.Button(frame1, text='6', width='3', command=lambda: numeroPulsado('6'))
botonX = tk.Button(frame1, text='X', width='3', command=lambda: multiplicar(numeroPantalla.get()))
boton4.grid(row=3, column=1)
boton5.grid(row=3, column=2)
boton6.grid(row=3, column=3)
botonX.grid(row=3, column=4)
# ------------------fila3-------------------------------
boton1 = tk.Button(frame1, text='1', width='3', command=lambda: numeroPulsado('1'))
boton2 = tk.Button(frame1, text='2', width='3', command=lambda: numeroPulsado('2'))
boton3 = tk.Button(frame1, text='3', width='3', command=lambda: numeroPulsado('3'))
botonmen = tk.Button(frame1, text='-', width='3', command=lambda: resta(numeroPantalla.get()))
boton1.grid(row=4, column=1)
boton2.grid(row=4, column=2)
boton3.grid(row=4, column=3)
botonmen.grid(row=4, column=4)
# ------------------fila4-------------------------------
boton0 = tk.Button(frame1, text='0', width='3', command=lambda: numeroPulsado('0'))
botoncoma = tk.Button(frame1, text=',', width='3', command=lambda: numeroPulsado(','))
botonigual = tk.Button(frame1, text='=', width='3', command=lambda: el_resultado())
botonsum = tk.Button(frame1, text='+', width='3', command=lambda: suma(numeroPantalla.get()))
boton0.grid(row=5, column=1)
botoncoma.grid(row=5, column=2)
botonigual.grid(row=5, column=3)
botonsum.grid(row=5, column=4)


raiz.mainloop()
