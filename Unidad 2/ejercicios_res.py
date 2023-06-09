#EJERCICIO 1
import sys

if int(sys.argv[1]) % 2 == 0:
    print("El primer parámetro es múltiplo de 2")
else:
    print("El primer parámetro NO es múltiplo de 2")
if int(sys.argv[2]) % 2 == 0:
    print("El segundo parámetro es múltiplo de 2")
else:
    print("El segundo primer parámetro NO es múltiplo de 2")
if int(sys.argv[3]) % 2 == 0:
    print("El tercer parámetro es múltiplo de 2")
else:
    print("El tercer parámetro NO es múltiplo de 2")
    
#EJERCICIO2

frutas = ["Peras", "Bananas"]

print(f"Necesito que me traigas del super las {frutas[0]} y {frutas[1]} que te pedi")
print("tengo dos tipos de frutas " + frutas[0] + " y " + frutas[1])

#EJERCICIO 3

valor1 = input("Inserte el valor1: ")
valor2 = input("Inserte el valor2: ")
lista = [valor1, valor2, int(valor1) + int(valor2)]
print(lista)

#EJERCICIO 4

edad = int(input("Ingrese su edad: "))
edad_jubilatoria = 65

if edad > edad_jubilatoria:
    print("Ya está en edad de jubilarse")
else:
    print("Aun esta en edad de trabajar")

#EJERCICIO 5


