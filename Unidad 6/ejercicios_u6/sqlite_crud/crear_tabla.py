import sqlite3

def crear_base():
    con = sqlite3.connect('mibase.db')
    return con

def crear_tabla(con):

    cursor = con.cursor()
    sql = "CREATE TABLE gentes(id integer PRIMARY KEY, nombre text)"
    cursor.execute(sql) #le mando la instruccion
    con.commit() #lo realiza

con = crear_base()
crear_tabla(con)
