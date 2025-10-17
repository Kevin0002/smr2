import random

def adivina_el_numero():
    """
    Este es un juego de adivinar el número.
    La computadora piensa en un número entre 1 y 100, y tú tienes que adivinarlo.
    """
    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    while not adivinado:
        try:
            intento_str = input("Tu adivinanza: ")
            intento = int(intento_str)
            intentos += 1

            if intento < numero_secreto:
                print("Demasiado bajo. ¡Intenta de nuevo!")
            elif intento > numero_secreto:
                print("Demasiado alto. ¡Intenta de nuevo!")
            else:
                adivinado = True
                print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    adivina_el_numero()
