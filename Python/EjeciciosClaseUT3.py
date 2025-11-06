# -*- coding: utf-8 -*-
"""
1) Mete los valores del 1 al 100 en una lista.
a) Imprimirlos ordenados
b) Imprimirlos al revés.
c) Pide un número por teclado y comprueba si se encuentra en la lista. En caso de que si esté
debe salir del bucle.
"""

# Creamos una lista con números del 1 al 100
lista = list(range(1, 101))

# a) Imprimimos la lista ordenada (ya lo está por defecto)
print("Lista ordenada:")
print(lista)

# b) Imprimimos la lista al revés
print("\nLista al revés:")
print(lista[::-1])

# c) Bucle para pedir números y comprobar si están en la lista
print("\nComprobar si un número está en la lista:")
while True:
    # Pedimos un número al usuario
    num = int(
        input("Introduce un numero y comprueba que este en la lista (0 para salir): ")
    )
    # Si el número es 0, salimos del bucle
    if num == 0:
        break
    # Comprobamos si el número está en la lista
    if num in lista:
        print(f"El numero {num} esta en la lista")
        break  # Salimos del bucle si el número se encuentra
    else:
        print(f"El numero {num} no esta en la lista")

print("\n" + "=" * 50 + "\n")

"""
2) Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo,
si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
"""
# Pedimos un número al usuario
num = int(input("Introduce un numero para ver su tabla de multiplicar: "))

# Creamos una lista con la tabla de multiplicar usando un bucle for y list comprehension
tablaMultiplicar = [num * i for i in range(1, 11)]

# Imprimimos la tabla de multiplicar
print(f"La tabla de multiplicar de {num} es: {tablaMultiplicar}")


print("\n" + "=" * 50 + "\n")


"""
3) Crea una lista vacía (pongamos 10 posiciones), pide sus valores y devuelve la suma y la media de
los números. 
"""
# Creamos una lista vacía
lista = []

# Bucle para pedir 10 valores
i = 0
while i < 10:
    # Pedimos un valor y lo convertimos a entero
    valor = int(input(f"Introduce el valor {i + 1}/10 a la lista: "))
    # Añadimos el valor a la lista
    lista.append(valor)
    i += 1

# Imprimimos la lista completa
print("Lista completa: ", lista)

# Calculamos la suma de los elementos de la lista
suma = sum(lista)
# Calculamos la media
media = suma / len(lista)

# Imprimimos la suma y la media
print(f"Suma de la lista: {suma}")
print(f"Media de la lista: {media}")

print("\n" + "=" * 50 + "\n")

"""
4) Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero. (while)
"""
# Creamos una tupla con los meses del año. La primera posición es un error para alinear los meses con los índices.
meses = (
    "ERROR",
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
)

# Bucle infinito hasta que el usuario introduzca un 0
while True:
    # Pedimos un número de mes
    i = int(input("Introduce un numero de un mes (0 para salir): "))
    # Si el número es 0, salimos del bucle
    if i == 0:
        break
    # Comprobamos si el número está en el rango válido (1-12)
    if i in range(1, 13):
        # Imprimimos el mes correspondiente
        print(meses[i])
    else:
        # Si no, imprimimos un error
        print(meses[0])

print("\n" + "=" * 50 + "\n")

"""
5) Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por
último, muestra los números ordenados de menor a mayor.
Usa el método sort para ordenar
"""
# Creamos una lista vacía
lista = []

# Bucle para pedir números hasta que se introduzca un 0
while True:
    valor = int(input("Introduce un valor a la lista (0 para parar): "))
    if valor == 0:
        break
    # Añadimos el valor a la lista
    lista.append(valor)

# Ordenamos la lista de menor a mayor
lista.sort()
# Imprimimos la lista ordenada
print(f"Lista ordenada de menor a mayor: {lista}")

print("\n" + "=" * 50 + "\n")

"""
6) Lo mismo que el anterior pero ordenando de mayor a menor.
"""
# Creamos una lista vacía
lista = []
# Bucle para pedir números hasta que se introduzca un 0
while True:
    valor = int(input("Introduce un valor a la lista (0 para parar): "))
    if valor == 0:
        break
    # Añadimos el valor a la lista
    lista.append(valor)

# Ordenamos la lista de mayor a menor
lista.sort(reverse=True)

# Imprimimos la lista ordenada
print(f"Lista ordenada de mayor a menor: {lista}")

print("\n" + "=" * 50 + "\n")

# Ejercicio 7: Cadena a lista sin espacios
print("=== Ejercicio 7 ===")
# Pedimos una cadena al usuario
cadena = input("Introduce una cadena: ")
# Creamos una lista vacía para guardar los caracteres sin espacios
lista_sin_espacios = []
# Recorremos cada caracter de la cadena
for caracter in cadena:
    # Si el caracter no es un espacio, lo añadimos a la lista
    if caracter != " ":
        lista_sin_espacios.append(caracter)
# Imprimimos la lista resultante
print("Lista sin espacios:", lista_sin_espacios)

print("\n" + "=" * 50 + "\n")

# Ejercicio 8: Cadena a lista sin repetir caracteres
print("=== Ejercicio 8 ===")
# Pedimos una cadena al usuario
cadena = input("Introduce una cadena: ")
# Creamos una lista vacía para guardar los caracteres sin repetir
lista_sin_repetir = []
# Recorremos cada caracter de la cadena
for caracter in cadena:
    # Si el caracter no está ya en la lista, lo añadimos
    if caracter not in lista_sin_repetir:
        lista_sin_repetir.append(caracter)
# Imprimimos la lista resultante
print("Lista sin repetir caracteres:", lista_sin_repetir)

print("\n" + "=" * 50 + "\n")

# Ejercicio 9: Contar repeticiones de un número en tupla
print("=== Ejercicio 9 ===")
# Definimos una tupla de números
numeros = (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)
# Imprimimos la tupla
print("Tupla:", numeros)
# Pedimos al usuario un número para contar
numero = int(input("Introduce un número para contar cuántas veces se repite: "))
# Usamos el método count() de las tuplas para contar las repeticiones
contador = numeros.count(numero)
# Imprimimos el resultado
print(f"El número {numero} se repite {contador} veces")

print("\n" + "=" * 50 + "\n")

# Ejercicio 10: Mayor y menor valor de una tupla
print("=== Ejercicio 10 ===")
# Definimos una tupla de números
numeros = (5, 4, 3, -2, 1, 6, 455, 3, 6, 6, 6, 6, 6)
# Imprimimos la tupla
print("Tupla:", numeros)

# Usamos las funciones max() y min() para encontrar el mayor y menor valor
mayor = max(numeros)
menor = min(numeros)

# Imprimimos el resultado
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
