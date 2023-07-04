from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
from PIL import ImageTk, Image
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
             legajo int,
             sector text,
             motivo_reclamo text,
             periodo int,
             )
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
    legajo.set("")
    sector.set("")
    motivo_reclamo.set("")
    periodo.set("")

def alta(nombre, apellido, legajo, sector, motivo_reclamo, periodo, tree):

    if askyesno("ATENCIÓN!!!", "Los datos ingresados son correctos?"):
        showinfo("Si", "Perfecto, a continuacoón se generará el alta")
        print(nombre, apellido, legajo, sector, motivo_reclamo, periodo)
        con=conexion()
        cursor=con.cursor()
        data=(nombre, apellido, legajo, sector, motivo_reclamo, periodo)
        sql="INSERT INTO empleados(nombre, apellido, legajo, sector, motivo_reclamo, periodo) VALUES(?, ?, ?, ?, ?, ?)"
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
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))


root = Tk()

root.title("REGISTRO DE RECLAMOS SOBRE EL RECIBO DE SUELDO")
root.configure(bg="#DA7777")
color_fondo = "#DA7777"
color_tit= "#F42107"
titulo = Label(root, text="INGRESE AQUÍ EL RECLAMO", bg=color_tit, fg="thistle1", height=1, width=80)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

titulo = Label(root, text="DETALLE DE RECLAMOS CARGADOS", bg=color_tit, fg="thistle1", height=1, width=80)
titulo.grid(row=9, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
print(BASE_DIR)
ruta = os.path.join(BASE_DIR, "img", "coca2.jpg")
image2 = Image.open("coca22.jpg")
print(image2)
image1 = ImageTk.PhotoImage(image2)
print(image1)
background_label = ttk.Label(root, image=image1)
background_label.place(x=50, y=32) #relwidth=1, relheight=1)

nombre = Label(root, text="Nombre", bg=color_fondo)
nombre.grid(row=4, column=0, sticky=W,)
apellido=Label(root, text="Apellido", bg=color_fondo)
apellido.grid(row=5, column=0, sticky=W)
legajo=Label(root, text="Legajo", bg=color_fondo)
legajo.grid(row=6, column=0, sticky=W)
sector=Label(root, text="Sector", bg=color_fondo)
sector.grid(row=4, column=2, sticky=W)
motivo_reclamo=Label(root, text="Motivo del reclamo", bg=color_fondo)
motivo_reclamo.grid(row=5, column=2,sticky=W)
periodo=Label(root, text="Periodo", bg=color_fondo)
periodo.grid(row=6, column=2, sticky=W)
e = Entry(root) 

nombre, apellido, legajo, sector, motivo_reclamo, periodo = StringVar(), StringVar(), IntVar(), StringVar(), StringVar(), IntVar()
w_ancho = 20

entrada1 = Entry(root, textvariable = nombre, width = w_ancho) 
entrada1.grid(row = 4, column = 1, padx=10, pady=10)
entrada2 = Entry(root, textvariable = apellido, width = w_ancho) 
entrada2.grid(row = 5, column = 1, padx=10, pady=10)
entrada3 = Entry(root, textvariable = legajo, width = w_ancho) 
entrada3.grid(row = 6, column = 1, padx=10, pady=10)
entrada4 = Entry(root, textvariable = sector, width = w_ancho) 
entrada4.grid(row = 4, column = 3, padx=10, pady=10)
entrada5 = Entry(root, textvariable = motivo_reclamo, width = w_ancho) 
entrada5.grid(row = 5, column = 3, padx=10, pady=10)
entrada6 = Entry(root, textvariable = periodo, width = w_ancho) 
entrada6.grid(row = 6, column = 3, padx=10, pady=10)


tree = ttk.Treeview(root)
tree["columns"]=("col1", "col2", "col3", "col4", "col5", "col6")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=100, minwidth=80)
tree.column("col2", width=100, minwidth=80)
tree.column("col3", width=100, minwidth=80)
tree.column("col4", width=100, minwidth=80)
tree.column("col5", width=100, minwidth=80)
tree.column("col6", width=100, minwidth=80)
tree.heading("col1", text="nombre")
tree.heading("col2", text="apellido")
tree.heading("col3", text="legajo")
tree.heading("col4", text="sector")
tree.heading("col5", text="motivo_reclamo")
tree.heading("col6", text="periodo")

tree.grid(row=10, column=0, columnspan=4)

color_botones = "#D62F1B"
boton_alta=Button(root, text="Generar", bg= color_botones, width=25, command=lambda:alta(nombre.get(), apellido.get(), legajo.get(), sector.get(), motivo_reclamo.get(), periodo.get(), tree))
boton_alta.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_consulta=Button(root, text="Consultar", bg= color_botones, width=25, command=lambda:consultar(tree))
boton_consulta.grid(row=2, column=2, sticky="e", padx=10, pady=10)

boton_borrar=Button(root, text="Borrar", bg= color_botones, width=25, command=lambda:borrar(tree))
boton_borrar.grid(row=3, column=2, sticky="e", padx=10, pady=10)

actualizar_treeview(tree)

root.mainloop()