"""
1) Mete los valores del 1 al 100 en una lista.
a) Imprimirlos ordenados
b) Imprimirlos al revés.
c) Pide un número por teclado y comprueba si se encuentra en la lista. En caso de que si esté
debe salir del bucle.
"""

lista = list(range(1, 101))
print(lista)

print(lista[::-1])

while True:
    num = int(input("Introduce un numero y comprueba que este en la lista: "))
    if num in lista:
        print(f"El numero {num} esta en la lista")
        break
    else:
        print(f"El numero {num} no esta en la lista")

"""
2) Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo,
si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
"""

num = int(input("Introduce un numero para ver su tabla de multiplicar: "))
tablaMultiplicar = [
    num,
    num * 2,
    num * 3,
    num * 4,
    num * 5,
    num * 6,
    num * 7,
    num * 8,
    num * 9,
    num * 10,
]

print("La tapla de multiplicar de {num} es: ", tablaMultiplicar)

"""
3) Crea una lista vacía (pongamos 10 posiciones), pide sus valores y devuelve la suma y la media de
los números. 
"""
lista = []

i = 0
while i < 10:
    valor = int(input("introduce un valor a la lista: "))
    lista.append(valor)
    i += 1

print("Lista completa: ", lista)

suma = sum(lista)
media = suma / len(lista)

print(f"Suma de la lista: {suma}")
print(f"Media de la lista: {media}")


"""
4) Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero. (while)
"""

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

while True:
    i = int(input("Introduce un numero de un mes: "))
    if i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        print(meses[i])
    else:
        print(meses[0])
        break

"""
5) Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por
último, muestra los números ordenados de menor a mayor.
Usa el método sort para ordenar
"""
lista = []

while True:
    valor = int(input("introduce un valor a la lista: "))
    if valor == 0:
        break

    lista.append(valor)

lista.sort
print(f"Lista ordenada de menor a mayor: {lista}")

"""
6) Lo mismo que el anterior pero ordenando de mayor a menor.
"""

lista = []
while True:
    valor = int(input("introduce un valor a la lista: "))
    if valor == 0:
        break

    lista.append(valor)

lista.sort(reverse=True)

print(f"Lista ordenada de mayor a menor: {lista}")

"""
7) Pide una cadena por teclado, mete los caracteres en una lista sin espacios.
"""

cadena = str(input("Ingrece una cadena de texto: "))
lista = [cadena]

lista.remove(" ")
print(f"Lista sin espacios: {lista}")
