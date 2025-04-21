"""A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el
programa deberá determinar la posición del jugador en la cancha, considerando los
siguientes parámetros:
● Menos de 160 cm: Base
● Entre 160 cm y 179 cm: Escolta
● Entre 180 cm y 199 cm: Alero
● 200 cm o más: Ala-Pívot o Pívot
2. Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un
mensaje según el valor:
● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
● 4 y 5 ---> Aprobado, la nota es ...
● 1, 2 y 3 ---> Desaprobado, la nota es ..."""

""""ejericio 1"""

altura_jugador = int(input("Ingrese la altura del Jugador: "))

if altura_jugador < 160:
    print("La posicion del jugador es Base")
elif altura_jugador >= 160 and altura_jugador <= 179:
    print("La posicion del jugador es Escolta")
elif altura_jugador >= 180 and altura_jugador <= 199:
    print("La posicion del jugador es Alero")
else:
    print("La posicion del jugador es Pívot") 

""""ejericio 2"""

#En caso de que se use el random
"""import random
promedio = random.randint(1, 10)"""


primera_nota = int(input("Ingresá la nota del primer examen (del 1 al 10): "))
segunda_nota = int(input("Ingresá la nota del segundo examen (del 1 al 10): "))

promedio = (primera_nota + segunda_nota) / 2

print(f"El promedio es {promedio}")

if promedio >= 6 and promedio <= 10:
    print(f"Promoción directa, la nota es {promedio}")
elif promedio >= 4:
    print(f"Aprobado, la nota es {promedio}")
elif promedio >= 1:
    print(f"Desaprobado, la nota es {promedio}")
else:
    print("Promedio inválido")
