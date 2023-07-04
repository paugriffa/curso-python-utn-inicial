from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
#from PIL import ImageTk, Image
import os
#import re

# conección con SQL
def conexion():
    con = sqlite3.connect("mibase.sqlite3")
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE empleados
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre text,
             apellido text,
             fecha_alta text)
    """
    cursor.execute(sql)
    con.commit()

#para saber si da error al crear la base
try:
    conexion()
    crear_tabla()
except:
    print("Hay un error")
    
def pregunta():
    if askyesno("ATENCIÓN!!!", "Los datos ingresados son correctos?"):
        showinfo("Si", "Perfecto, a continuacoón se generará el alta")
    else:
        showinfo("No", "Proceda a cargarlos nuevamente")

def reseteo():
    nombre.set("")
    apellido.set("")
    fecha_alta.set("")

def alta(nombre, apellido, fecha_alta, tree):

    if askyesno("ATENCIÓN!!!", "Los datos ingresados son correctos?"):
        showinfo("Si", "Perfecto, a continuacoón se generará el alta")
        print(nombre, apellido, fecha_alta)
        con=conexion()
        cursor=con.cursor()
        data=(nombre, apellido, fecha_alta)
        sql="INSERT INTO empleados(nombre, apellido, fecha_alta) VALUES(?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
        reseteo()
    else:
        showinfo("No", "Proceda a cargarlos nuevamente")


def consultar(tree):
    valor = tree.selection()
    print(valor)
    item = tree.item(valor)
    print(item)
    print(item['text'])
    mi_id = item['text']
    con=conexion()
    cursor = con.cursor()
    data = (mi_id,)
    sql = "SELECT * FROM empleados WHERE ID =?;"
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']

    con=conexion()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM empleados WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)

def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM empleados ORDER BY id DESC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

root = Tk()

root.title("Empleados")
titulo = Label(root, text="Ingrese los datos", bg="DarkOrchid3", fg="thistle1", height=1, width=80)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

# BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
# ruta = os.path.join(BASE_DIR, "img", "coca.jpg")
# image2 = Image.open(ruta)
# print(image2)
# image1 = ImageTk.PhotoImage(image2)
# print(image1)
# background_label = tk.Label(app, image=image1)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

nombre = Label(root, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)
apellido=Label(root, text="Apellido")
apellido.grid(row=2, column=0, sticky=W)
fecha_alta=Label(root, text="Fecha Alta")
fecha_alta.grid(row=3, column=0, sticky=W)
e = Entry(root) 

nombre, apellido, fecha_alta, region = StringVar(), StringVar(), StringVar(), StringVar()
w_ancho = 30

entrada1 = Entry(root, textvariable = nombre, width = w_ancho) 
entrada1.grid(row = 1, column = 1)
entrada2 = Entry(root, textvariable = apellido, width = w_ancho) 
entrada2.grid(row = 2, column = 1)
entrada3 = Entry(root, textvariable = fecha_alta, width = w_ancho) 
entrada3.grid(row = 3, column = 1)


tree = ttk.Treeview(root)
tree["columns"]=("col1", "col2", "col3")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=80)
tree.column("col2", width=200, minwidth=80)
tree.column("col3", width=200, minwidth=80)
tree.column("col4", width=200, minwidth=80)
tree.column("col5", width=200, minwidth=80)
tree.column("col6", width=200, minwidth=80)
tree.heading("col1", text="nombre")
tree.heading("col2", text="apellido")
tree.heading("col3", text="legajo")
tree.heading("col4", text="fecha_alta")
tree.heading("col5", text="puesto")
tree.heading("col5", text="fecha_alta")

tree.grid(row=10, column=0, columnspan=4)

color_botones = "#D62F1B"
boton_alta=Button(root, text="Generar alta", bg= color_botones, command=lambda:alta(nombre.get(), apellido.get(), fecha_alta.get(), tree))
boton_alta.grid(row=6, column=0)

boton_consulta=Button(root, text="Consultar", bg= color_botones, command=lambda:consultar(tree))
boton_consulta.grid(row=6, column=1)

boton_borrar=Button(root, text="Borrar", bg= color_botones, command=lambda:borrar(tree))
boton_borrar.grid(row=6, column=2)

actualizar_treeview(tree)

root.mainloop()