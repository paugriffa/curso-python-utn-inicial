import sqlite3
from sqlite3 import Error
# ############# CREAR BASE DE DATOS

#si esta creada, la lee, sino la crea y no da error
def crear_base():

    con = sqlite3.connect('mibase.db')
    return con

crear_base()

