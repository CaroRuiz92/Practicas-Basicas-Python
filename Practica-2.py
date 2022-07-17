# Se tienen dos habitaciones dentro de un hogar, cada una con una temperatura ambiente. Se quiere
# saber a qué temperatura estarán las habitaciones, dado suficiente tiempo para que se transmita
# el calor de una a la otra. Se conoce que en este caso es válido promediar temperaturas.

temp1 = int(input("Ingrese temperatura 1: "))
temp2 = int(input("Ingrese temperatura 2: "))
print("El promedio de la temperatura es:",(temp1 + temp2) / 2)

# Se tiene una multitud afuera, cada persona le dirá su nombre a cada otra persona en la multitud.
# Se quiere saber cuánto tiempo llevará hacer esto, dado que decir una vez tu nombre lleva
# aproximádamente 4 segundos y medio.

cantidad = int(input("Ingrese cantidad de personas: "))
print("El tiempo que se tarda es:", (cantidad - 1) * 4.5, "segundos.")

# Hay dos personas con nombres muy largos, pero similares. 
# Se quiere conocer, por un lado, si tienen el mismo tamaño, y por otro lado si son iguales. 
# Ayuda para el programa: buscar la función len

nombre1 = input("Ingrese un nombre: ")
nombre2 = input("Ingrese otro nombre: ")
if len(nombre1) == len(nombre2):
    print("Los nombres ingresados tienen la misma cantidad de letras.")
else:
    print("Los nombres tienen diferente cantidad de letras.")
if nombre1 == nombre2:
    print("Los nombres son iguales.")
else:
    print("Los nombres no son iguales.")


# Traducir las siguientes expresiones del lenguaje natural a expresiónes booleanas en equivalentes
# en Python. Determinar su veracidad o falsedad corriendo la expresión en el intérprete.


#a. La longitud de la cadena "Hola, mundo" es 14.
cadena = "Hola, Mundo"
print(len(cadena) == 14)

#b. El área de un cuadrado de lado 5 es igual a la raíz cudrada de 625.
area = 5
print(area**2 == 625**1/2)

#c. El diametro de un circulo de radio 3,25 es menor que 7 y mayor a 6.
print(6<(3.14*(3.25)**2)<7)

#d. La apromixación de Pi = 22 / 7 es un número mayor que 3, y 2 + 2 es igual a 5.
print((22/7)<3 and (2+2) == 5)

#e. El numero 10 es mayor a 5 o 0 dividido 0 es igual 0.
print((10>5) or (0/0==0))

#f. La cadena "Python" tiene longitud 5 y 1+"1" es igual a 2.
print(len("Python")==5 and (1+"1")==2)







