from tkinter import *

master = Tk()


def hola():
    print("Hola")


menubar = Menu(master) #defino la variable donde pongo el munu

menu_archivo = Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Abrir", command=hola)
menu_archivo.add_command(label="Guardar", command=hola)
menu_archivo.add_separator() #separador de opciones
menu_archivo.add_command(label="Salir", command=master.quit) #al apretarlo hace que salga
menubar.add_cascade(label="Archivo", menu=menu_archivo)

menu_edicion = Menu(menubar, tearoff=0)
menu_edicion.add_command(label="Abrir", command=hola)
menu_edicion.add_command(label="Guardar", command=hola)
menu_edicion.add_separator()
menu_edicion.add_command(label="Salir", command=master.quit)
menubar.add_cascade(label="Editar", menu=menu_edicion)

submenu = Menu(menu_edicion, tearoff=True) #tearoff=True para un solo menu
submenu.add_command(label="Editar color", command=hola)
submenu.add_command(label="Rotar", command=hola)
menu_edicion.add_cascade(label="Otros", menu=submenu)

master.config(menu=menubar) #le paso a la ventana el menu, para que me lo muestre
master.mainloop()
