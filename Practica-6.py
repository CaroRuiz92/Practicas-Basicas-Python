# -*- coding: utf-8 -*-

# Nota: Esta práctica es para ejercitar la creación de funciones, por lo tanto, 
# deben usarse las mismas para resolver los ejercicios. 


# 1. Realizar una función que calcule la suma de dos números. En el algoritmo principal le pediremos
# al usuario que ingrese por consola los dos números para pasárselos a la función. 
# Después la función calculará la suma y lo devolverá para imprimirlo en el algoritmo.

def suma(a,b):
    sum = a+b
    return sum

print(suma(10,5))


# 2. Realizar una función que valide si un número es impar o no. 
# Si es impar la función debe devolver un verdadero, si no es impar debe devolver falso. 
# Nota: la función no debe tener mensajes que digan si es par o no, eso debe pasar en el Algoritmo.

def im_par(num):
    if num%2==0:
        return True
    else:
        return False
    
print(im_par(6))


# 3. Escribir una función que calcule la longitud de una cadena. Nota: no utilizar la función len.

def long_string(cadena):
    cont = 0
    for letra in cadena:
        cont+=1
    return cont

print(long_string("carolina"))


# 4. Escribir una función que recibe los catetos de un triángulo y calcule su hipotenusa.

def hipotenusa(cat1,cat2):
    hip = ((cat1**2+cat2**2)**(1/2))
    return hip

print(hipotenusa(3,5))


# 5. Escribir una función que calcule la distancia entre dos puntos en el plano. 
# Los puntos deberán ingresar a la función como tuplas.

def distancia(p1,p2):
    dist = ((p1[1]-p1[0])**2 + (p2[1]-p2[0]))**(1/2)
    return dist

print(distancia((3,5),(5,3)))


# 6. Realizar un programa que pida al usuario una frase y una letra a buscar en esa frase. 
# La función debe devolver la cantidad de veces que encontró la letra.

def contar_letras(frase, letra):
    cont = 0
    for l in frase:
        if l == letra or l == letra.upper():
            cont +=1
        else:
            continue
    return cont

print(contar_letras("La casa de Ana", "a"))


# 7. Un número es primo si solo si sus únicos divisores son 1 y el mismo número.
# a. Escriba una función que determine si un numero es primo o no.
# b. Escriba otra función que reciba un número n e imprima todos los números primos menores que n.

#a
def primo(num):
    div = []
    for n in range(1,num+1):
        if num%n==0:
            div.append(n)
        else:
            continue
        
    if len(div) == 2:
        return "Es primo"
    else:
        return "No es primo"

print(primo(29))


#b
def primos(num):
    primos = []
    for n in range(2,num):
        if primo(n) == "Es primo":
            primos.append(n)
    return primos

print(primos(10))


# 8. Escriba una función potencia que reciba dos números x y n, con n entero no negativo, que calcule x**n.

def potencia(x, n):
    if n > 0:
        return x**n
    else:
        return "El segundo número debe ser un entero positivo."
    
print(potencia(2,2))


# 9. Escribir una función que reciba una lista de números 
# y retorne una lista con los números pares y otra con los números impares.

def par_impar(*args):
    par = []
    impar = []
    for n in args:
        if n%2==0:
            par.append(n)
        else:
            impar.append(n)
    print(par)
    print(impar)

par_impar(2,3,4,5,6,7,8,9,10)


# 10. Realizar un menú similar a una calculadora. Funciones:
# 1. Suma(num1, num2)
# 2. Resta(num1, num2)
# 3. Division(num1, num2)
# 4. Multiplicacion(num1, num2)
# 5. Factorial(num)
# 0. Salir    

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def division(num1, num2):
    return num1/num2

def multiplicacion(num1, num2):
    return num1*num2

def factorial(num1, num2=0):
    fact = 1
    for i in range(1,num1+1):
        fact *=i
    return fact
    

def calculadora():
    ing = int(input("""
        Ingrese la función que quiere usar:
        1. Suma.
        2. Resta.
        3. Division.
        4. Multiplicacion.
        5. Factorial.
        0. Salir 
        """
     ))
    
    while ing != 0:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        if ing == 1:
            resultado = suma(num1,num2)
        elif ing == 2:
            resultado = resta(num1,num2)
        elif ing == 3:
            resultado = division(num1,num2)
        elif ing == 4:
            resultado = multiplicacion(num1, num2)
        elif ing == 5:
            resultado = factorial(num1,num2)
        else:
            break
        print(resultado)
        ing = int(input("""
            Ingrese la función que quiere usar:
            1. Suma.
            2. Resta.
            3. Division.
            4. Multiplicacion.
            5. Factorial.
            0. Salir 
            """
         ))
        
    
print(calculadora()) 


# 11. Escribir un programa de Python que le permita al usuario ingresar la fecha y hora de despegue 
# de dos vuelos y devuelva la diferencia en minutos entre los mismas. 
# El ingreso de la fecha y hora debe tener el formato ‘DD/MM/AAAA - hh:mm:ss‘.
# Desafío extra: Validar la fecha y hora ingresada. Por ejemplo, el mes no puede ser superior a 12, 
# la fecha no puede ser en el futuro, las horas no pueden ser mayores a 24, etc.

def diferencia_vuelos():
    print("Introduzca la información pedida sobre el primer vuelo:")
    fecha1 = input("Ingrese fecha: ")
    hora1 = input("Ingrese hora y minutos: ") 

    print("Introduzca la información pedida sobre el segundo vuelo:")
    fecha2 = input("Ingrese fecha: ")
    hora2 = input("Ingrese hora y minutos: ")

    
    dia1 = int(fecha1[:2])
    mes1 = int(fecha1[3:5])
    año1 = int(fecha1[-2:])
    h1 = int(hora1[:2])
    min1 = int(hora1[-2:])
    
    dia2 = int(fecha2[:2])
    mes2 = int(fecha2[3:5])
    año2 = int(fecha2[-2:])
    h2 = int(hora2[:2])
    min2 = int(hora2[-2:])
    
    if dia1 < 32 and mes1 < 13:
        if dia2 < 32 and mes2 < 13:
            dif_dia = int(dia2 - dia1)
            dif_mes = int(mes2 - mes1)
            dif_año = int(año2 - año1)    
            dif_hora = int(h2 - h1)
            dif_min = int(min2 - min1)
        else:
            print("Hay datos incorrectos")
    
    return "La diferencia entre vuelos es de:", dif_dia, "dias", dif_mes, "meses", dif_año, "años", dif_hora, "horas", dif_min, "minutos"

print(diferencia_vuelos()) # REVER












