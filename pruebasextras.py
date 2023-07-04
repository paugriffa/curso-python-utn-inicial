import sqlite3

def conexion():
    con = sqlite3.connect("mibase.db")
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


con = conexion()
crear_tabla(con)
