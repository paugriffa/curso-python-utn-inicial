"""
Ejercicio 5
Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), 
pero tratando de utilizar una función, de forma que la operación se realice dentro de la misma. 
Presente el resultado en la terminal del editor.

"""
valor=int(input("Ingrese un valor: "))

def calcular_incremento(val):
    resultado=val*1.1
    return resultado

print(calcular_incremento(valor))
