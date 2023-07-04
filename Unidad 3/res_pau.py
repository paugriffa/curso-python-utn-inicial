#Ejercicio 1

"""
Ejercicio 1 (Este es el ejercicio 2 de la unidad 1 pero implementando if/else):
Cree un programa que incorpore el módulo sys, al cual desde la terminal 
se le puedan pasar tres parámetros. El programa debe tomar los parámetros
e indicar en la terminal si son múltiplos de dos. Utilice la estructura if/else
"""
# import sys
# variable = sys.argv[1:]
# print(variable)


# for i in variable:
#     if int(i)%2 == 0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")

# """Ejercicio 2. Escriba un programa que consulte al usuario por una oración 
# y comente al usuario cuantas veces aparece la letra “a”. 
# """
# oracion = input("Escriba la oración que desee:")

# contador = 0

# for i in oracion:
#     if i == "a":
#         contador += 1
# print(contador)

# """Escriba un programa que consulte al usuario por una oración y comente al usuario 
# cuantas veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.  
# """

# oracion = input("Escriba la oración:")
# vocales = ["A", "E", "I", "O", "U"]
# contador = 0

# for i in oracion:
#     if i.upper() in vocales:
#         contador += 1
# print(contador)

# Ejercicio 4
# edad = int(input("Cuantos años tiene? "))

# for i in range(1,edad+1):
#     print("La persona tiene " + str(i) + " años")

# Ejercicio 5

# eleccion = input("Ingrese i si desea inicar o f si desea finalizar la carga: ")
# total=0


# if eleccion=="i":
#     seguir = True
# else:
#     seguir = False

# eleccion = ""
# total = 0
# lista_compras = []

# while eleccion != "x":
#     producto, cantidad, precio = input("Ingrese el producto, cantidad y precio, separados por espacio: ").split()
#     total += float(cantidad) * float(precio)
#     lista_compras.append([producto, cantidad, precio])
#     eleccion = input("Ingrese x solo si desea salir del programa: ")

# print("El total gastado es ", total)
# print(lista_compras)
# for x in lista_compras:
#     print("Producto: ", x[0], "Cantidad: ", x[1], "Precio: ", x[2])

# eleccion = ""
# total = 0
# dic_compras = {}
# num_dic = 0

# while eleccion != "x":
#     producto, cantidad, precio = input("Ingrese el producto, cantidad y precio, separados por espacio: ").split()
#     total += float(cantidad) * float(precio)
#     dic_compras[num_dic] = {"producto": producto,"cantidad": cantidad, "precio": precio}
#     num_dic+= 1
#     eleccion = input("Ingrese x solo si desea salir del programa: ")

# print("El total gastado es ", total)
# print(dic_compras)

# for key, values in dic_compras.items():
#     total = dic_compras["cantidad"] * dic_compras["precio"]
#     print(total)

eleccion = input("Ingrese i si desea inicar o f si desea finalizar la carga: ")
total=0


if eleccion=="i":
    seguir = True
else:
    seguir = False

eleccion = ""
total = 0
lista_compras = []

while eleccion != "x":
    producto, cantidad, precio = input("Ingrese el producto, cantidad y precio, separados por espacio: ").split()
    total += float(cantidad) * float(precio)
    lista_compras.append([producto, cantidad, precio])
    eleccion = input("Ingrese x solo si desea salir del programa: ")

print("El total gastado es ", total)
print(lista_compras)
for x in lista_compras:
    print("Producto: ", x[0], "Cantidad: ", x[1], "Precio: ", x[2])