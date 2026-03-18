#Traemos la funcion para poner un numero en aleatorio

import random

secret_number = random.randint(1, 100)
#limitar el numero de intentos
intentos = 0

#definir maximo de intentos
MaxIntentos = 5


print(secret_number)
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
|El maximo de intentos es: 5     |
+================================+
""")


while intentos < MaxIntentos:
    guess = int(input("Ingrese su numero: "))
    intentos += 1

    if guess == secret_number:
        print("🎉 ¡Ganaste!")
        break
    elif guess < secret_number:
        print("Muy bajo!")
    else: 
        print("Muy alto!")
if guess != secret_number:
    print("Perdiste el numero secreto es:", secret_number)