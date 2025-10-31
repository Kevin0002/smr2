"""
1) Mete los valores del 1 al 100 en una lista. 
a) Imprimirlos ordenados
b) Imprimirlos al revés.
c) Pide un número por teclado y comprueba si se encuentra en la lista. En caso de que si esté
debe salir del bucle.
"""

lista =list(range(1, 101))
print(lista)

print(lista[::-1])

while True:
    num=int(input("Introduce un numero y comprueba que este en la lista: "))
    if num in lista:
        print(f"El numero {num} esta en la lista")
        break
    else:
        print(f"El numero {num} no esta en la lista")

"""
2) Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo,
si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
"""

num=int(input("Introduce un numero para ver su tabla de multiplicar: "))
tablaMultiplicar = [num, num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10]

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

print("Lista completa: ",lista)

suma = sum(lista)
media = suma / len(lista)

print(f"Suma de la lista: ", suma)
print(f"Media de la lista: ", media)
