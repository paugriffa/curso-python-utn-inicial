from tkinter import *

master = Tk() #esta tk es unica por aplicacion

#label se usa para los niveles
el_id = Label(master, text="id") 

el_id.grid(row=0, column=0, sticky=W) #pongo el elemento en una grilla
#lo hago en dos renglones asi puedo modificar el label, cambiarle el color
nombre = Label(master, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)

entry_id = Entry(master)
entry_id.grid(row=0, column=1)
entry_nombre = Entry(master)
entry_nombre.grid(row=1, column=1)


master.mainloop()
