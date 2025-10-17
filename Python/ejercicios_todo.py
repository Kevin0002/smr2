# Ejercicios Elementales Unidad 1
# 1. Escribe un programa que muestre tu nombre por pantalla.
print ("Kevin\n")
# 2. Modifica el programa anterior para que además se muestre tu dirección y tu número de
# teléfono. Asegúrate de que los datos se muestran en líneas separadas.
print("Kevin\n","calle no importa 28\n",634273819)
# 3. Escribe un programa que pinte por pantalla una pirámide rellena a base de asteriscos. La
# base de la pirámide debe estar formada por 9 asteriscos.
print("    *")
print("   ***")
print("  *****")
print(" *******")
print("*********")
# 4. [Enteros] Crea un programa que pida dos números enteros por teclado y muestre todas las
# operaciones básicas (suma, resta, multiplicación, división, resto y potencia).
num = input("Ingrese el primer número: ")
num1 = input("Ingrese el segundo número: ")
operacion = input("Ingrese que operecion quiere realizar: +, -, *, /, **: ")
if operacion == "+":
    print("El resultado es: ", int(num) + int(num1))
elif operacion == "-":
    print("El resultado es: ", int(num) - int(num1))
elif operacion == "*":
    print("El resultado es: ", int(num) * int(num1))
elif operacion == "/":
    print("El resultado es: ", int(num) / int(num1))
elif operacion == "**":
    print("El resultado es: ", int(num) ** int(num1))
else:
    print("Operación no válida")
# 5. [Float] Escribe un programa que almacene una variable con el valor 1,3 e imprime por
# pantalla el número con 20 decimales. ¿Hay un error?
num = 1.3
print(f"{num:.20f}")
# 6. [Float] Escribe un programa que:
# Haga un redondeo más cercano con dos dígitos
# Redondeo hacia arriba
# Redondeo hacia abajo
# 7. Realizar un programa que pida una cantidad de segundos, los pase a minutos y, estos, a
# segundos. Tendrás que mostrar estos tres valores.
# 8. [Boolean] Visita la página w3scools apartado boolean y realiza el test final
# https://www.w3schools.com/python/python_booleans.asp
# 9. [Operadores] Visita la página w3scools apartado operators y realiza el test final
# https://www.w3schools.com/python/python_operators.asp
# 10. Un programa pedirá al usuario que introduzca los grados centígrados actuales. Tras
# introducirlos, los pasará a grados Fahrenheit: F = ( C * 1,8) + 32.
# 11. Calcula la longitud (2*PI*R) y el área de un círculo (PI*R2) a partir de un radio dado.
# 12. Una farmacia quiere hacer un descuento en productos del 10%. Realizar un programa que
# muestre el nuevo precio de un artículo dado.
# 13. Un programa que lea la cantidad de alumnos y de alumnas que hay en tu clase de
# programación, y tras procesarlo, mostrará el porcentaje correspondiente a cada género.
# 14. El nuevo banco nacional, va a aplicar un 20% de interés a todos sus usuarios. Calcula cuál
# será la cantidad final de dinero que tendrás tras aplicar este interés.
# 15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
# algoritmo que intercambie los valores de ambas variables y muestre cuánto valen al final las
# dos variables
# 16. Los porcentajes de cada uno de los trimestres de programación para este nuevo curso serán
# 20%, 30% у 50% respectivamente. Realiza un programa que calcula la nota final de un
# alumno, aplicando estos porcentajes, a partir de sus notas parciales
# 17. [String] Escribe una variable con el valor “En un lugar de la mancha de cuyo nombre no
# quiero acordarme ...” y realiza las siguientes operaciones:
# Comprueba sin la palabra mancha se encuentra dentro del texto. Imprime el resultado
# Añade al texto con el operador + “dijo Don Quijote:” y el resto del texto. Imprime el
# resultado
# Imprime 3 veces el texto usando el operador *
print("Hola\n" * 3)
# Imprime la longitud del texto
# Imprime la primera letra
# Imprime la cuarte letra
# Imprime la última letra
# Imprime del principio hasta la 10
# Imprime entre la 10 y la 15
# Imprime de la 20 al final
# Pon todo el texto en mayúsculas. Imprime el resultado
# 18. Explica para que sirve la función f.string y pon un ejemplo
