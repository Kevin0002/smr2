nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
print(f"Hola, {nombre} {apellido}!")

numero = 10

print(type(numero))

f = float(input("Ingresa los grados Fahrenheit: "))
c = (f - 32) * 5/9
print(f"{f} grados Fahrenheit son {c:.2f} grados Celsius.")