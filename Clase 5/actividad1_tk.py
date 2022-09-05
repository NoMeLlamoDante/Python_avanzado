from tkinter import *
from tkinter import ttk

#Crear Ventana
root = Tk()
root.title("Activdad 1")

#Funcion
def pasar_texto(*args):
    salida.set(entrada.get())

#Padding: Izquierda, derecha Arriba y abajo
mainframe = ttk.Frame(root,width=30, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Variables 
entrada = StringVar()
salida = StringVar()

#Entrada
ttk.Entry(mainframe, textvariable=entrada).grid(column=1, columnspan=2, row=1, sticky=(W, E))

#Label
ttk.Label(mainframe, width=15,textvariable=salida).grid(column=1, row=2, sticky=(W, E))

#Boton 
ttk.Button(mainframe, width=15, text="Guardar", command=pasar_texto ).grid(column=2, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#Enter As button
root.bind("<Return>", pasar_texto)

root.mainloop()