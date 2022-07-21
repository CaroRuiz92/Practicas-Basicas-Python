# 1.1 Dada la base B y la altura H de un rectangulo, informar el area y el perÄ±metro.
# 1.2 Pedir el valor de 3 variables, realizar y mostrar el resultado de:
# a. La suma de las dos primeras
# b. El producto de las dos ultimas
# c. Reemplazar el valor de la 3ra. por el triple de la primera

b = 12  #1.1
h = 6
print(f"El Area es: {b*h}")
print(f"El peri­metro es: {(b*2)+(h*2)}")

a = int(input("Ingresar un valor:"))  #1.2
b = int(input("Ingresar otro valor:"))
c = int(input("Ingresar un  ultimo valor:"))

print(f"La suma de los dos primeros valores es {a+b}")
print(f"El producto de los dos Ãºltimos es: {b*c}")
c = a*3
print(c)

# 2.1 Se ingresa un numero por teclado:
# a. Informar si es positivo o negativo.
# b. Informar si es par o impar.
# 2.2 Dado dos numeros enteros N y M, informar si N es multiplo de M.

a = int(input("Ingresar un valor:"))
if a%2==0:
    if a>0:
        print("Tu nÃºmero es par y positivo.")
    else:
        print("Tu nÃºmero es par y negativo.")
else:
    if a>0:
        print("Tu nÃºmero es impar y positivo.")
    else:
        print("Tu nÃºmero es impar y negativo.")

n = int(input("Ingresar un valor:"))
m = int(input("Ingresar otro valor:"))      
if m%n==0:
    print("El primero es mÃºltiplo del otro.")
else:
    print("No son mÃºltiplos entre sÃ­")

# 3.1 Solicitar un numero del 1 al 7 y diga el dia de la semana correspondiente. 
# Suponga que el lunes es el primer dia.
# 3.2 Solicitar una letra y detecte si es una vocal.

n = int(input("Ingrese un numero: "))

if n == 1:
    print("Lunes")
elif n == 2:
    print("Martes")
elif n == 3:
    print("MiÃ©rcoles")
elif n == 4:
    print("Jueves")
elif n == 5:
    print("Viernes")
elif n == 6:
    print("SÃ¡bado")
elif n == 7:
    print("Domingo")
else:
    print("Su valor es incorrecto.")

n = input("Ingrese una letra: ")
if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
    print("Es una vocal.")
else:
    print("Es una consonante.")
 

# 4.1 Mostrar 10 veces el texto "Estoy probando".

for i in range(10):
    print("Estoy probando")

# 4.2 Modificar el algoritmo anterior para mostrar: âEstoy probando 1â, âEstoy probando 2â, ..., hasta 10.
# Codificar en lenguaje Python y ejecutar el programa. Verificar los resultados.

for i in range(1,11):
    print(f"Estoy probando {i}")


# 4.3 Mostrar los numeros del 0 al 100.

for i in range(101):
    print(i)

# 4.4 Pedir 10 numeros y mostrar la suma de los pares y de los impares por separado. 
#Verificar los resultados utilizando la calculadora.

a = int(input("Ingresar un valor:"))
b = int(input("Ingresar otro valor:"))
c = 0
d = 0
for n in range(a,(b+1)):
    if n%2==0:
        c = c+n
    elif n%2!=0:
        d = d+n
print("La suma de los pares es",c)
print("La suma de los impares es",d)

# 4.5 Contar e informar los numeros multiplos de 2 o 3 que hay entre 1 y 100. Verificar el resultado.

dos = []
tres = []

for n in range(1,101):
    if n%2==0:
        dos.append(n)
    elif n%3==0:
        tres.append(n)
print(dos)
print(f"Hay {len(dos)} multiplos de dos.")
print(tres)
print(f"Hay {len(tres)} multiplos de tres.")

# 4.7 Dado 10 numeros, informar el rango de los mismos [menor, mayor].

for n in range(1,11):
    print(f"{n-1},{n},{n+1}")

# 4.8 Se ingresan 10 numeros. Determinar el promedio de los mismos.

m = 0
for n in range(1,11):
    m = m+n
print(f"Resultado: {m}. El promedio es {m/10}")

# 5.1 Programa que pregunte iterativamente “¿Quiere continuar?”, con respuesta S o N.

c = 1
while c > 0:
    s = input("¡Hola! ¿Quiere continuar? Si/No: ")
    if s == "si":
        s = input("¡Hola! ¿Quiere continuar? Si/No")
    else:
        break
print("Fue un placer")

# 5.2 Dadas las notas de los estudiantes que rindieron un examen, 
# informar el porcentaje de notas superiores a 7. 
# El docente desconoce la cantidad que asistio a rendir.

nota = input("Ingrese la nota del alumno. Cuando termine de ingresarlas, escriba 'salir': ")
aprob = 0
ing = 0
while nota != "salir":
    ing +=1
    nota = int(nota)
    if nota >= 7:
        aprob += 1
    elif nota < 7:
        pass
    else:
        break
    nota = input("Ingrese la nota del alumno. Cuando termine de ingresarlas, escriba 'salir': ")

print("El promedio de alumnos aprobados es de", ((aprob*100)/ing))
    
# 5.3 Los pediatras registran edad, estatura y peso de niños que atienden 
# en el Hospital de Niños Vilela de la ciudad de Rosario. 
# Con esos datos se puede calcular el Índice de masa corporal IMC. 
# El IMC deben ser de cuidado pues si está por debajo de 12 
# puede haber desnutrición en el niño, y por arriba de 20, sobrepeso u obesidad. 
# El cálculo del mismo es: 
# IMC = Peso en kilogramos / Estatura en centímetro² 
# Se pide escribir un algoritmo que recibiendo los datos del médico determine 
# el porcentaje de niños de un año con posible desnutrición que se atendieron el último mes. 

print("""
CALCULADORA DE IMC
Ingrese peso en kgs y luego estatura en cm.
Para terminar, ingrese salir
""")
conf = input("¿Iniciar? si - no: ")

while conf != "no":
    peso = int(input("Peso: "))
    est = int(input("Estatura: "))
    imc = (peso / (est**2))
    if imc < 12:
        print("Debajo de 12. Se presenta desnutrición.")
    elif imc < 12 and imc > 20:
        print("Entre 12 y 20: nivel saludable.")
    elif imc > 20:
        print("Supera los 20. Se presenta sobrepeso u obesidad.")
    else:
        break
    conf = input("¿Reiniciar? si - no: ")

print("Calculadora: OFF")
