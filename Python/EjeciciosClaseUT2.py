"""
1. Diseña un programa que te pida tu edad e indique si eres mayor de edad
o no. Usa constantes para definir la edad que corresponde con la mayoría
de edad.
"""

"""
edad=int(input("Introduce tu edad: "))
MAYORIA_DE_EDAD=18


if edad>=MAYORIA_DE_EDAD:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")"""

"""
2. Diseñar un programa que pida por teclado dos números enteros y un
menú que muestre las opciones de suma, resta, multiplicación, división y
el resto (módulo) de la división.
Muestra el resultado correspondiente, si la operación no es conmutativa,
también se mostrará el resultado invirtiendo los operadores
"""

"""
num1=int(input("Introduce el primer número entero: "))
num2=int(input("Introduce el segundo número entero: "))

operacion=(input("Elige una operación (+, -, *, /, %): "))

if operacion=="+":
    print(f"El resultado de {num1} + {num2} es: {num1 + num2}")
elif operacion=="-":
    print(f"El resultado de {num1} - {num2} es: {num1 - num2}")
    print(f"El resultado de {num2} - {num1} es: {num2 - num1}")
elif operacion=="*":
    print(f"El resultado de {num1} * {num2} es: {num1 * num2}")
elif operacion=="/":
    if num2!=0:
        print(f"El resultado de {num1} / {num2} es: {num1 / num2}")
    else:
        print("Error: División por cero no permitida.")
elif operacion=="%":
    if num2!=0:
        print(f"El resultado de {num1} % {num2} es: {num1 % num2}")
    else:
        print("Error: División por cero no permitida.")
else:
    print("Operación no válida")
"""

"""
3. Programa que lee dos números y muestra el mayor en pantalla. Si son
iguales deberá mostrar un mensaje indicándolo.
"""

"""
num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Los dos números son iguales")
"""

"""
Programa que lea 3 números y que los imprima ordenados de mayor a
menor.
"""

"""
num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
num3=int(input("Introduce el tercer número: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(f"Los números ordenados de mayor a menor son: {num1}, {num2}, {num3}")
    else:
        print(f"Los números ordenados de mayor a menor son: {num1}, {num3}, {num2}")
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(f"Los números ordenados de mayor a menor son: {num2}, {num1}, {num3}")
    else:
        print(f"Los números ordenados de mayor a menor son: {num2}, {num3}, {num1}")
else:
    if num1 >= num2:
        print(f"Los números ordenados de mayor a menor son: {num3}, {num1}, {num2}")
    else:
        print(f"Los números ordenados de mayor a menor son: {num3}, {num2}, {num1}")
"""


