import random


def juego_adivinanza():
    # Generar un número de 1 a 100 para adivinarlo atraves de un input
    numero_secreto = random.randint(1, 101)
    intentos = 0
    adivinado = False

    # Primeras líneas del juego
    print("Bienvenido al juego de adivinar número!")
    print("Debes adivinar un número del 1 al 100")
    print("Intenta adivinarlo!")

    while not adivinado:
        # Solicitar un numero del 1 al 100
        adivinanza = input("Introduzca un número del 1 al 100:")  # es un string

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # pasamos de string a numero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones, has ganado! El número {adivinanza} es el número secreto y solo te tomó {intentos} intentos."
                )
        else:
            print("Por favor: introduzca un número válido entre 1 y 100")


juego_adivinanza()
