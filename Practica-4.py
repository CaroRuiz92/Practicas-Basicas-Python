# Imprimir los primeros 20 números naturales.

for nro in range(1,21):
    print(nro)

# Imprimir la tabla de multiplicar del número 5

for x in range(11):
    print(f"5 x {x} =", x*5)

# Imprima los números de -10 a -1.

for x in range(-10,0):
    print(x)

# Dada la siguiente secuencia de números:
# numeros = [12 , 75 , 150 , 180 , 145 , 525 , 50]
# imprimir los números divisibles por 5 menores a 150

for n in [12 , 75 , 150 , 180 , 145 , 525 , 50]:
    if n < 150:
        if n % 5 == 0:
            print(n)
    else:
        continue

# Imprimir los primeros 10 valores de la secuencia de Fibonacci. La secuencia de Fibonacci es una serie
# de números en la cual los dos primeros números son 0 y 1, y el siguiente número se corresponde a la
# suma de los dos números anteriores. Resultado esperado:
# 0 1 1 2 3 5 8 13 21 34

prim = 0
seg = 1
print(prim)
print(seg)
for i in range(8):
    ter = prim + seg
    print(ter)
    prim = seg
    seg = ter

# Imprimir el valor factorial del número 5 usando un bucle. 
# El valor factorial (símbolo: !) se obtiene de multiplicar todos los números enteros 
# desde el número elegido hasta 1. Resultado esperado: 120

#Con for:
    
f = 1
for i in range(1,6):
	f = f * i
print(f)

#Con while:

f = 1
m = 1
while True:
	if f < 120:
		f = f*m
		m += 1
	else:
		break
print(f)  

# Resuelva los siguientes ejercicios
# a. Calcular el cuadrado de los primeros 10 números enteros.
# b. Calcular la suma de los números enteros entre 0 y 100 inclusive.
# c. Calcular la suma de los números pares menores a 100. 
# ¿Cuántos números pares hay menores a 100?
# d. Calcular la suma de los números impares menores a 100. 
# ¿Cuántos números impares hay menores a 100?

for n in range(11):  #a
    n = n**2
    print(n)

m = 0
for n in range(101):  #b
    m += n
    print(m)

m = 0
for n in range(0,100,2):  #c
    m += n
    print(m)
print("Entre 0 y 100 hay",len(range(0,100,2)), "números pares")

m = 0
for n in range(1,101,2):  #d
    m += n
    print(m)
print("Entre 0 y 100 hay",len(range(1,101,2)), "números impares")


# Escriba un programa que dada una secuencia de números y un valor de umbral 
# vaya sumando los números de la secuencia hasta que la suma alcance el umbral. 
# Utilice break para terminar la ejecución del bucle cuando la suma alcance el umbral.
# Ejemplo:
# umbral = 21
# valores = [3, 5, 4, 4, 5, 5, 3, 5, 2, 7]
# suma -> 21

cont = 0
for i in [3, 5, 4, 4, 5, 5, 3, 5, 2, 7]:
    while cont < 21:
        cont += i
print("Con umbral: 21 y con valores [3, 5, 4, 4, 5, 5, 3, 5, 2, 7]. Suma:", cont)

# Escriba un programa que dada una secuencia numérica compute la suma de los números pares. 
# Utilice un bucle while y la sentencia continue para saltear los casos donde el número no sea par.
# Resultados esperados:
# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# suma -> 30

# Version 1:
cont = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i % 2 == 0:
        cont += i
print(cont)

# Version 2:
cont = 0
while cont < 30:   #rever
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        if i%2==0:
            cont += i
        else:
            continue
print(cont)

# Escriba un programa que solicite un numero entero al usuario y compute la suma de todos los numeros
# naturales menores a él. Este programa debe ser interactivo. 
# Es decir, el programa solicita un numero al usuario, devuelve la suma, y solicita un nuevo número. 
# Esto continúa así hasta que el usuario ingresa "salir", determinando que el programa debe terminar. 
# Utilice un bucle while para resolver este problema. 
# Tenga en cuenta la sentencia break para determinar la interrupción del bucle. 
# Ejemplos:
# Ingrese un numero o 'salir ' para terminar : 10
# La suma es 45
# Ingrese un numero o 'salir ' para terminar : 50
# La suma es 1225
# Ingrese un numero o 'salir ' para terminar : salir

ing = input("Ingrese un número o salir para terminar: ")
while ing != "salir":
	cont = 0
	for i in range(1,int(ing)+1):
		cont += i
	print(cont)
	ing = input("Ingrese un número o salir para terminar: ")

# Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera. 
# A partir de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente. 
# ¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que la del Monumento? 
# Considere los siguientes valores para comenzar a resolver el problema:

# billete_grosor = 0.11 * 0.001 # grosor de un billete en metros
# altura_monumento = 70 # altura en metros
# billetes_n = 1
# dia = 1
# Utilice un bucle while para resolver el problema.

billete_grosor = 0.11 * 0.001 # grosor de un billete en metros
altura_monumento = 70 # altura en metros
billetes_n = 1
dia = 1

alt = 0
while alt < altura_monumento:
    alt += (billetes_n * billete_grosor)
    billetes_n *=2
    dia +=1

print("Llegar a la altura del monumento toma", dia, "días")
print("Para esto se necesitarían", billetes_n, "billetes")

# Escriba un programa reciba dos números como parámetros, y compute 
# cuántos múltiplos del primero hay, que sean menores que el segundo.

prim = int(input("Ingrese un número: "))
seg = int(input("Ingrese otro número: "))
res = []

for i in range(0,seg):
    cont = 0
    cont = prim * i
    if cont < seg:
        res.append(cont)
print("Los múltiplos de", prim, "menores que", seg, "son", str(res))

