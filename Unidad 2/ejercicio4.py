"""
Ejercicio 4
Realice un programa que consulte la edad y en caso de que el valor 
ingresado supere la fecha de jubilación, presente en la terminal el mensaje 
“Ya está en edad de jubilarse” en caso contrario que presente “Aún está en edad de trabajar”

"""
edad=int(input("Ingrese un valor: "))
if edad<=63:
    print("Estás en edad de trabajar")
else:
    print("Tendrías que jubilarte")    