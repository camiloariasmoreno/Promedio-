import random
MIN=1
MAX=100

# Generar un número secreto entre 1 y 100
numero_secreto = random.randint(MIN,MAX)

intentos = 0
adivino = False

while intentos < 6 and not adivino:

    print(f"\nIntento {intentos + 1} de 6")

    numero_usuario = int(input("Ingrese un número entre 1 y 100: "))

    intentos += 1

    if numero_usuario == numero_secreto:
        print("¡Correcto!")
        adivino = True

    elif numero_usuario > numero_secreto:
        print("El número es menor")

    else:
        print("El número es mayor")

# Si no adivinó después de los 6 intentos
if not adivino:
    print(f"\nPerdiste, el número era {numero_secreto}")
    



