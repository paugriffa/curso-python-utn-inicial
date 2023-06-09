#Escriba un programa que solicite el  el radio de una circunferencia y permita calcular el
# perímetro. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# L = 2 · π · r
# L = Longitud de perímetro
# π = Número pí igual a 3.1416
# r = Radio 

radio = input("Ingrese el radio de una circunferencia: ")
π = 3.1416
resultado = int(radio) * π * 2
print(resultado)

# Escriba un programa que solicite el radio de una circunferencia y permita calcular el
# área. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# 𝐴 = 𝜋. 𝑟ଶ
# A = Área

radio2 = input("Ingrese el radio de una circunferencia: ")
π = 3.1416
area = int(radio2) * π
print(area)

# Ejercicio 5:
# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal del
# editor el valor incrementado en un 10%.

valor = input("Ingrese el valor deseado: ")
print(int(valor) * 2)
