"""
Ejercicio 1 (Este es el ejercicio 2 de la unidad 1 pero implementando if/else):
Cree un programa que incorpore el módulo sys, al cual desde la terminal 
se le puedan pasar tres parámetros. El programa debe tomar los parámetros
 e indicar en la terminal si son múltiplos de dos. Utilice la estructura if/else
"""
import sys
variable = sys.argv
print(variable)
#['ejercicio1.py', '3', '4', '5']
varible1=int(variable[1])
varible2=int(variable[2])
varible3=int(variable[3])

if varible1%2==0:
    print("El valor ingresado es par")
else:
    print("El valor ingresado es impar")

if varible2%2==0:
    print("El valor ingresado es par")
else:
    print("El valor ingresado es impar")

if varible3%2==0:
    print("El valor ingresado es par")
else:
    print("El valor ingresado es impar")