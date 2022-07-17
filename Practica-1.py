# Dada la base y altura de un rectangulo, informar el area y su perımetro.

base = int(input("Ingresa la base: "))
alt = int(input("Ingresa la altura: "))
rectangulo = [base, alt]

area = rectangulo[0] * rectangulo[1]
perimetro = ((rectangulo[0])*2) + ((rectangulo[1])*2)
print(area)
print(perimetro)


# Calcular la nota final de un alumno que se obtiene de promediar las 3 notas de sus parciales.

nota = [5, 7, 9]

promedio = (nota[0] + nota[1] + nota[2]) / len(nota)
print(promedio)

# Calcular la distancia de dos puntos en el plano.

import math

punto1 = [2, 3, 5]
punto2 = [3, 4, 6]

resta_x = punto2[0] - punto1[0]
resta_y = punto2[1] - punto1[1]
resta_z = punto2[2] - punto1[2]

r = [resta_x, resta_y, resta_z]
print(r)
modulo = math.sqrt(((r[0])**2 + (r[1])**2 + (r[2])**2)) # RECORDAR: MATH.SQRT
print(modulo)










