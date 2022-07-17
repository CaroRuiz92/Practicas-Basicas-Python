# Dada una contraseÃ±a verificar que su longitud es superior a 8 caracteres.

contra = input("Ingrese su contraseÃ±a: ")
if len(contra) > 8:
    print("Su contraseÃ±a es superior a 8 caracteres.")
else:
    print("Su contraseÃ±a tiene 8 caracteres o menos.")


# Escribir un programa que verifique si un numero es divisible por 4

num = float(input("Ingrese un nÃºmero: "))

if num % 4 == 0:
    print("El nÃºmero ingresado es divisible por 4.")
else:
    print("El nÃºmero no es divisible por 4.")


# Determinar e informar el mayor valor de 3 numeros enteros. 
# Â¿Que cambiarÄ±as en el algoritmo si se trataran de 3 numeros reales
#  o de 3 caracteres o de 3 palabras?. Â¿Y si se buscara el menor valor?

num = [3, 4, 7]
print(max(num))
print(min(num))


# Dados 3 lados de un triangulo, informar si el mismo es equilatero, isosceles o escaleno.

lados = [19,29,19]

if lados[0] == lados[1] == lados[2]:
    print("Tenemos un triÃ¡ngulo equilatero.")
elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
    print("Tenemos un triÃ¡ngulo isÃ³sceles.")
else:
    print("Tenemos un triÃ¡ngulo escaleno.")


# Convertir las calificaciones alfabeticas I€™, A€™, B€™, M€™, D€™ y E€™ en calificaciones numericas 5, 6, 7, 8, 9 y
# 10 respectivamente. Ingresar una calificacion alfabÂ´etica e informar por pantalla la calificacion numerica
# correspondiente, en caso de ingresar cualquier otra letra mostrar ((error calificacion inexistente)).

nota = input("Ingresar su nota alfabética: ")

if nota == "I":
    print("Nota: 5 (cinco)")
elif nota == "A":
    print("Nota: 6 (seis)")
elif nota == "B":
    print("Nota: 7 (siete)")
elif nota == "M":
    print("Nota: 8 (ocho)")
elif nota == "D":
    print("Nota: 9 (nueve)")
elif nota == "E":
    print("Nota: 10 (diez)")
else:
    print("Calificación inexistente")
    

"""
En el centro de la ciudad de Rosario el estacionamiento en výa se encuentra tarifado y esta dividido
en tres zonas con tarifas diferenciadas. El vehýculo puede estacionarse como maximo por 3 horas en
el mismo sitio, luego de este tiempo, para renovar el servicio, hay que mover el vehýculo. La siguiente
tabla muestra los costos por hora en cada una de las zonas:
    
Zona Primer hora Segunda hora Tercer Hora
A    $57,00          $71,20      $85,50
B    $47,00          $58,70      $70,50
C    $37,00          $46,20      $55,50
Escribir un programa que dada la zona, A, B o C, y la cantidad de horas que el vehýculo estara
estacionado, devuelva el costo a pagar. En caso de que el tiempo de estacionamiento supere las 3 horas,
imprimir un mensaje de error acorde.
"""

z = input("Ingrese la zona: ")
h = int(input("Ingrese la cantidad de tiempo: "))
cont = 0

while z !=0 and h != 0:
    if z == "A":
        if h == 1:
            print("$57")
        elif h == 2:
            print("$71,20")
        elif h == 3:
            print("$85,50")
        else:
            print("Hubo un error. Intente de nuevo.")
            cont =+ 1
        z = input("Ingrese la zona: ")
        h = int(input("Ingrese la cantidad de tiempo: "))
    elif z == "B":
        if h == 1:
            print("$47")
        elif h == 2:
            print("$58,70")
        elif h == 3:
            print("$70,50")
        else:
            print("Hubo un error. Intente de nuevo.")
            cont =+ 1
        z = input("Ingrese la zona: ")
        h = int(input("Ingrese la cantidad de tiempo: "))
    elif z == "C":
        if h == 1:
            print("$37")
        elif h == 2:
            print("$46,20")
        elif h == 3:
            print("$55,50")
        else:
            print("Hubo un error. Intente de nuevo.")
            cont =+ 1
        z = input("Ingrese la zona: ")
        h = int(input("Ingrese la cantidad de tiempo: "))
else:
    print("Alguno de los datos brindados son incorrectos.")


# Una marca de ropa tienen descuentos diferentes dependiendo de la sede del local:
# Item            Rosario      Funes      Roldan
# Zapatillas      30%           40%        25%
# Remeras         20%           30%        15%
# Pantalones      10%           5%         20%
# Dado un item y la sede del local, devolver el descuento que se recibira. 

s = input("Ingrese la sede: ")
i = input("Ingrese el item: ")
cont = 0

if s == "Rosario":
    if i == "zapatillas":
        print("30%")
    elif i == "remeras":
        print("20%")
    elif i == "pantalones":
        print("10%")
        
elif s == "Funes":
    if i == "zapatillas":
        print("40%")
    elif i == "remeras":
        print("30%")
    elif i == "pantalones":
        print("5%")
        
elif s == "Roldán":
    if i == "zapatillas":
        print("25%")
    elif i == "remeras":
        print("15%")
    elif i == "pantalones":
        print("20%")
        
else:
    while s != "Rosario" or s!= "Funes" or s!= "Roldan" or i != "zapatillas" or i != "remeras" or i!= "pantalones":
        print("Hubo un error. Intente de nuevo.")
        cont =+ 1
        s = input("Ingrese la sede: ")
        i = input("Ingrese el item: ")
       ## REVER FINAL




