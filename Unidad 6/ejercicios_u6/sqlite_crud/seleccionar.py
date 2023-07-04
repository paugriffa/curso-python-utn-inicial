
import sqlite3


def crear_base():
    con = sqlite3.connect('mibase.db')
    return con

def seleccionar(con, mi_id):
    cursor = con.cursor()
    mi_id = int(mi_id)
    data = (mi_id,) #la coma es para que lo tome como tupla sino da error
    sql = "SELECT * FROM personas WHERE id =?;"
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


con = crear_base()

seleccionar(con, 3)




def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)