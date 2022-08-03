                    ### Listas ###

# 1.a Dada una lista de números list y un número n, determine en qué índice de la lista list se
# encuentra el número n. En caso de no encontrarlo, el programa mostrará -1. 
# Ejemplos
# list = [11 ,25 ,3 , -4 ,95]
# n = 3
# El programa debería mostrar 2
# list = [1 ,2 ,3 ,4 ,5]
# n = 10
# El programa debería mostrar -1

# Versión 1:
list = [11 ,25 ,3 , -4 ,95]
for index, value in enumerate(list):
    if value == 3:
        print(index)
    else:
        print(-1)

# Versión 2:
ing = int(input("Ingrese un valor que podría estar en la lista. Si la respuesta es -1, no está: "))
for index, value in enumerate(list):
    if value == ing:
        print("El valor está en la ubicación", index)
    else:
        print(-1)


# 1.b Dada una lista de números, calcule el mínimo y el máximo de la lista. 
# Nota: es posible hacerlo recorriendo una única vez la lista o recorriéndola dos veces. 
# Piense las ventajas y desventajas de ambos métodos.
# numeros = [11 ,25 ,3 , -4 ,95]
# El programa debería mostrar
# El mínimo es -4
# El máximo es 95

numeros = [11, 25, 3, -4, 95]

min = 0
for i in numeros:
    if i < min:
        min = i
    else:
        continue
print("El mínimo es", min)   

max = 0
for i in numeros:
    if i > max:
        max = i
    else:
        continue
print("El máximo es", max)


# 1.c Dada una lista de números, cree una nueva lista sumando 1 a cada elemento.
# numeros = [0 ,1 ,2 ,3 ,4]
# El programa debería mostrar
# [1 ,2 ,3 ,4 ,5]

lista = []
numeros = [0 ,1 ,2 ,3 ,4]

for i in numeros:
    lista.append(i+1)

print(lista)


# 1.d Dada una lista palabras de cadenas de texto, devuelva una nueva lista formada 
# sólo por las cadenas de palabras que empiezan con "a".
# palabras = [" arbol ", " barco ", " artificial ", " casa ", " dado ", "a"]
# El programa debería mostrar
# [" arbol ", " artificial ", "a"]

palabras = ["arbol", "barco", "artificial", "casa", "dado", "a"]
lista = []

for i in palabras:
    if i[0] == "a":
        lista.append(i)
    else:
        continue
print(lista)


# 1.e Dada una lista de números, calcule, por un lado, la suma de los elementos 
# que se encuentran en un índice par en la lista y, por otro lado, 
# el producto de los elementos de posiciones con índice impar.
# numeros = [0 ,1 ,2 ,3 ,4 ,5]
# El programa debería mostrar
# La suma de índices pares es 6
# El producto de índices impares es 15

numeros = [0, 1, 2, 3, 4, 5]
sum_par = 0
sum_impar = 1

for index, value in enumerate(numeros):
    if index%2==0:
        sum_par += value
    else:
        sum_impar *= value
        
print("La suma de índices pares es", sum_par)
print("El producto de índices impares es", sum_impar)


# 1.f Dada una lista cualquiera, cree una nueva lista 
# con los mismos elementos pero en el orden inverso.
# numeros = [0 ,1 ,2 ,3 ,4 ,5]
# El programa debería mostrar
# [5 ,4 ,3 ,2 ,1 ,0]

# Versión 1:
numeros = [0, 1, 2, 3, 4, 5]   
print(sorted(numeros, reverse=True))

#Version 2:
lista = []
num = numeros[-1]
for i in range(0,6):
    if i <= num:
        lista.append(num-i)

print(lista)


# 2. Escriba un programa que dada una lista de números list devuelva otra lista cuyos elementos sean las
# sumas acumuladas de los elementos de list en cada posición. Es decir, una nueva lista donde el primer
# elemento es el mismo que en la lista original list, el segundo elemento es la suma del primer y segundo
# elementos de list, el tercer elemento es la suma del resultado anterior con el tercer elemento de la
# lista original y así sucesivamente. 
# Por ejemplo, dada la lista [1, 2, 3], la suma acumulada debería ser [1, 3, 6].

lista = [1, 2, 3]
acum = []
cont = 0

for i in lista:
    acum.append(i + cont)
    cont +=i
print(acum)


# 3. Escriba un programa que dada una lista determine si tiene algún elemento repetido e imprimirlos.
# Puede asumir que un numero se repite a lo sumo una vez. Pista: Utilice slicing de listas.

lista = [1,8,3,4,5,6,1,8,5]
temp = []
repets = []

for i in lista:   #Rever con slicing
    if i not in temp:
        temp.append(i)
    else:
        repets.append(i)

print(repets)


# 4. Calcule los n primeros números de la secuencia de Fibonacci en una lista. 
# Es decir, el programa comenzara con la lista [0,1] 
# y computará iterativamente el siguiente número de la secuencia.

num = int(input("Ingrese cuántos números quiere ver de la secuencia de Fibonacci: "))
lista = [0,1]
fibo  = [0,1]

for i in range(0,num-2):
    fibo.append(lista[0] + lista[1])
    lista[0] = fibo[i+1]
    lista[1] = fibo[i+2]
print(fibo)


# 5. El objetivo de este ejercicio es recolectar datos de personas 
# y almacenarlos en una especie de base de datos. 
# A través de lo diferentes ítems, los iremos guiando en la creación de la misma.

# a. Escribir un programa que le pida al usuario ingresar por consola los siguientes datos por separado:
# Nombre, Apellido, Localidad, Edad, DNI, Carrera universitaria en curso, año de inicio de la carrera. 
# Guardar los datos en una lista llamada datos_personales e imprimirlos en pantalla.

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
localidad = input("Ingresar localidad: ")
edad = int(input("Ingrese edad: "))
dni = int(input("Ingrese DNI sin comas, espacios o puntos: "))
carrera = input("Ingrese Carrera Universitaria: ")
año = int(input("Ingrese el año de inicio de la carrera: "))

datos_personales = [nombre, apellido, localidad, edad, dni, carrera, año]
print(datos_personales)


# b. A partir de la lista del ejercicio anterior, 
# genere un programa que calcule los años que la persona lleva cursando la carrera 
# y lo agregue a la lista. Por ejemplo, si la persona inició su carrera en el 2019, 
# la cantidad de años cursados a agregar es 4.
# Finalmente, imprima una frase que indique el nombre, el apellido y cantidad de años cursados de la persona

años_curs = 2022-datos_personales[6]
datos_personales.append(años_curs)
print(datos_personales[0],datos_personales[1],datos_personales[-1])


# c. Utilice el código de los ítems de arriba y automatice la recolección de datos 
# para una cantidad de personas desconocidas. 
# El resultado de este ejercicio debe ser una lista llamada basedatos donde
# se almacenarán las listas datos_personales de cada individuo que se recolecten

basedatos = []
ing = input("¿Quiere ingresar datos de alumnos? ")

while ing != "no":
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    localidad = input("Ingresar localidad: ")
    edad = int(input("Ingrese edad: "))
    dni = int(input("Ingrese DNI sin comas, espacios o puntos: "))
    carrera = input("Ingrese Carrera Universitaria: ")
    año = int(input("Ingrese el año de inicio de la carrera: "))
    pers = [nombre, apellido, localidad, edad, dni, carrera, año, 2022-año]
    basedatos.append(pers)
    ing = input("¿Quiere ingresar datos de alumnos? ")
print(basedatos)


# d. Realice un programa que modifique para cada persona la carrera en curso por la palabra "TUIA".

for i in basedatos:
    i[5] = "TUIA"

print(basedatos)



                    ### Tuplas ###

# Un analista económico utiliza un programa que toma desde una tupla valores 
# de la cotización en pesos del dolar blue en los últimos 5 días:
# dolarBlue = ( "189 "," 1930 "," 187 "," 210 "," 202 ")
# con el propósito de utilizarlos en un determinado informe. El programador se ha dado cuenta de que
# necesita modificar la segunda posición del mismo, porque hay un error de entrada del dato. 
# ¿Qué solución propone para enmendar este problema?

dolarBlue = ("189","1930","187","210","202")
print(dolarBlue)

blue = []
for i in list(dolarBlue):
    blue.append(int(i))

ind = int(input("Ingrese el index que quiere cambiar: "))
ing = int(input("Ingrese el valor nuevo: "))

for index, value in enumerate(blue):
    if index == ind:
        blue[ind] = ing
    else:
        continue
blue_def = tuple(blue)
print(blue_def)


# Dada una lista de tuplas donde el elemento en la posición 0 es el DNI de la persona 
# y en la posición 1 es el ingreso, identificar todas las personas cuyo ingreso es:
# a. Menor que el salario mínimo, vital y móvil (SMVM)
# b. Entre un SMVM y dos SMVM
# c. Entre dos SMVM y 4 SMVM
# d. Mayor a 4 SMVM
# Crear una lista de tuplas donde el primer elemento indica el rango de ingresos 
# y el segundo elemento la cantidad de personas en ese segmento.

base = [(33333333, 75000), (44444444, 55000), (55555555, 600000), (66666666, 100000), (77777777, 40000), (88888888, 500000)]
smvm = 45540

for tupla in base:
    if tupla[1] < smvm:
        print("La persona que cobra menos que el SMVM es la persona con el DNI:", tupla[0])
    elif (tupla[1] >= (smvm*2)) and (tupla[1] < (smvm*4)):
        print("La persona de DNI", tupla[0], "cobra entre dos SMVM y 4 SMVM.")
    elif tupla[1] > (smvm*4):
        print("La persona con DNI", tupla[0], "cobra más que 4 SMVM.")
    else:
        continue



                    ### Diccionarios ###

# Escribe un programa que lea una cadena y devuelva un diccionario 
# con la cantidad de apariciones de cada palabra en la cadena. 
# Por ejemplo:
# "la peluca de la abuela"
# Deber ía mostrar
# {"la": 2 , " peluca ": 1 , "de": 1 , " abuela ": 1}

palabras = "la peluca de la abuela"
lista = palabras.split()

dic = {}

for palabra in lista:
    if palabra not in dic:
        dic[palabra] = 1
    else:
        dic[palabra] +=1

print(dic)


# Escribir un programa que recibe un diccionario que 
# tiene como llave a alumnos y los valores asociados
# una lista con las notas de parciales de los alumnos. 
# El programa debe calcular el promedio de cada
# alumno e imprimirlo en pantalla. 
# Por ejemplo para
# alumnos = {" Juan ": [6 ,9 ,8] , " Manuel ": [9 ,10 ,9] , " Martin ": [5 ,6 ,7]}
# Debería mostrar
# El promedio de Juan es 7.666666
# El promedio de Manuel es 9.333333
# El promedio de Martin es 6

alumnos = {"Juan": [6, 9, 8] , "Manuel": [9, 10, 9] , "Martin": [5, 6, 7]}

for alumno in alumnos:
    lista = []
    lista = alumnos[alumno]
    print("El promedio de", alumno, "es", sum(lista)/len(lista))


# Repita el ejercicio 3 pero utilizando un diccionario:
# Ahora un número puede repetirse varias veces.
# Escriba un programa que dada una lista determine 
# si tiene algún elemento repetido e imprimirlos.

lista = [1,1,1,2,2,3,3,3,4,4,4,4,5,2,3,6]

dic = dict.fromkeys(lista, 0)

for i in lista:
    if dic[i] in dic:
        dic[i] +=1
    else:
        dic[i] = 1
print(dic)


# Dadas dos listas donde la primera contiene nombres de personas y la segunda sus edades,
# generar un diccionario a partir de ellas. 
# Investigar cómo la función zip() puede ayudar en la resolución

nombres = ["Carla", "Ana", "Fernanda", "Camila"]
edades = [14, 26, 39, 55]

dic = dict(zip(nombres, edades))
print(dic)


# Dado un diccionario donde la clave es el DNI (formato cadena) 
# y el valor es la cantidad de dosis de
# vacunas contra el covid, filtrar del mismo las personas que tienen 2 dosis 
# y guardarlas en la estructura de datos que crea conveniente. 
# Esta información será uilizada para recordarles 
# que ya tienen disponible la tercera dosis.

base = {"11111111": 2, "22222222": 1, "33333333": 3, "444444444": 2, "55555555": 1, "66666666": 2}
avisar = []
for clave in base:
    if base[clave] == 2:
        avisar.append(clave)
    else:
        continue
print(avisar)


# Un investigador de historia de la informática encontró un documento sin membrete, que data de
# mitad de siglo XX, e incluye un mensaje en código morse que sospecha explicaría importantes sucesos
# históricos de la posteridad. Por lo tanto, para avanzar en su investigación es necesario descifrarlo, 
# pero no sabe el código. Dado el siguiente diccionario que permite descifrar un mensaje morse, 
# ayude al investigador en su tarea mediante un programa que le permita decodificar el mensaje.

morse = {
'A': '. -', 'B': ' -... ', 'C': ' -. -. ',
'D': ' -.. ', 'E': '.', 'F': '.. -. ',
'G': ' - -.', 'H': '.... ', 'I': '.. ',
'J': '. - - -', 'K': ' -. -', 'L': '. -.. ',
'M': '--', 'N': ' -.', 'O': '---',
'P': '. - -. ', 'Q': ' - -. -', 'R': '. -. ',
'S': '... ', 'T': '-', 'U': '.. - ',
'V': '... - ', 'W': '. - -', 'X': ' -.. - ',
'Y': ' -. - -', 'Z': ' - -.. ', '1': '. - - - -',
'2': '.. - - - ', '3': '... - - ', '4': '.... - ',
'5': '..... ', '6': ' -.... ', '7': ' - -... ',
'8': ' - - -.. ', '9': ' - - - -.', '0': ' -----',
'.': '. -. -. - ', ',': ' - -.. - - ', ':': ' - - -... ',
';': ' -. -. -. ', '?': '.. - -.. ', '!': ' -. -. - - ',
'"': '. -.. -. ', "'": '. - - - -. ', '+': '. -. -. ',
'-': ' -.... - ', '/': ' -.. -. ', '=': ' -... - ',
'_': '.. - -. - ', '$': '... -.. - ', '@': '. - -. -. ',
'&': '. -... ', '(': ' -. - -. ', ')': ' -. - -. - '
}

codigo = ['.', ' -.', '.. - -. - ', '.', '. -.. ', '.. - -. - ', '.. -. ', '.. - ', '-', '.. - ',
'. -. ', '---', '.. - -. - ', '.', '... ', '.. - -. - ', '. - -. ', '---', '... ',
'.. ', ' -... ', '. -.. ', '.', '.. - -. - ', ' - -. -', '.. - ', '.', '.. - -. - ',
'. -.. ', '---', '... ', '.. - -. - ', '---', '. -. ', ' -.. ', '.', ' -.',
'. -', ' -.. ', '---', '. -. ', '.', '... ', '.. - -. - ', ' -.', '---',
'.. - -. - ', '. - -. ', '.', '... ', '.', ' -.', '.. - -. - ', '--', '. -',
'... ', '.. - -. - ', ' -.. ', '.', '.. - -. - ', '. - - - -', ' - -.. - - ', '..... ',
'.. - -. - ', '-', '---', ' -.', '.', '. -.. ', '. -', ' -.. ', '. -', '... ',
'. -. -. - ', '.. - -. - ', ' -.... - ', ' -.... - ', '.. - -. - ', '. - -. ', '---',
'. - -. ', '.. - ', '. -.. ', '. -', '. -. ', '.. - -. - ', '--', '.', ' -. -. ',
'.... ', '. - -. ', '.. ', ' -. -. ', '... ', ' - -.. - - ', '.. - -. - ', '. - - - -',
' - - - -.', '.... - ', ' - - - -.', ' - - -... ']

msj = []
for elem in codigo:
    for clave in morse:
        if elem == morse[clave]:
            msj.append(clave)
        else:
            continue

msj_final = ""
for elem in msj:
    msj_final += elem

print(msj_final)


# Cada profe de programación 1 tiene un diccionario donde guarda el legajo de cada alumno 
# en la clave y una lista con las notas de cada persona en el valor. 
# Al cerrar el cuatrimestre, necesitan pasarle a alumnado un solo diccionario con estos datos, 
# generarlo. Revisar el método .update() para ver como puede ayudarte a resolver el problema. 
# Los diccionarios de cada comisión se ven así
# com1 = {'legajo_11 ': [6 , 7 , 8] ,... , 'legajo_1m ': [3 , 8 , 9]}
# com2 = {'legajo_21 ': [6 , 7 , 8] ,... , 'legajo_2n ': [3 , 8 , 9]}
# com3 = {'legajo_31 ': [6 , 7 , 8] ,... , 'legajo_3j ': [3 , 8 , 9]}
# com4 = {'legajo_41 ': [6 , 7 , 8] ,... , 'legajo_4k ': [3 , 8 , 9]}

com1 = {"legajo_11": [6 , 7 , 8], "legajo_1m": [3 , 8 , 9], "legajo_11m": [3 , 8 , 7]}
com2 = {"legajo_21": [6 , 7 , 8], "legajo_2n": [3 , 8 , 9], "legajo_22n": [3 , 8 , 6]}
com3 = {"legajo_31": [6 , 7 , 8], "legajo_3j": [3 , 8 , 9], "legajo_33j": [5 , 9 , 9]}
com4 = {"legajo_41": [6 , 7 , 8], "legajo_4k": [3 , 8 , 9], "legajo_44k": [6 , 7 , 9]}

base = (com1, com2, com3, com4)
prog_1 = {}

for dic in base:
    prog_1.update(dic)
    
print(prog_1)






