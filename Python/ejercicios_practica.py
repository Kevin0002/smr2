# -*- coding: utf-8 -*-

# Ejercicio 1: Suma de dos números
# Escribe una función que tome dos números como argumentos y devuelva su suma.
def sumar(a, b):
  suma = a + b
  return suma
  pass

# Ejercicio 2: Contar del 1 al 10
# Escribe un bucle que imprima los números del 1 al 10.
def contar_diez():
  for i in range(1, 11):
    print(i)
  pass

# Ejercicio 3: Número par o impar
# Escribe una función que tome un número como argumento y devuelva "par" si el número es par y "impar" si es impar.
def es_par_o_impar(numero):
  if numero % 2 == 0:
    return "par"
  else:
    return "impar"
  pass

# Ejercicio 4: Invertir una cadena
# Escribe una función que tome una cadena de texto y devuelva la cadena invertida.
def invertir_cadena(cadena):
  return cadena[::-1]
  pass

# Ejercicio 5: Encontrar el máximo
# Escribe una función que tome una lista de números y devuelva el número más grande de la lista.
def encontrar_maximo(lista):
  if not lista:
    return None  # Manejar el caso de lista vacía
  maximo = lista[0]
  for numero in lista:
    if numero > maximo:
      maximo = numero
  return maximo
  pass

# --- Zona de pruebas ---
# Puedes usar esta sección para probar tus funciones.
print("Probando Ejercicio 1 (sumar):")
print(f"La suma de 5 y 3 es {sumar(5, 3)}")

print("\nProbando Ejercicio 2 (contar_diez):")
contar_diez()

print("\nProbando Ejercicio 3 (es_par_o_impar):")
print(f"El número 4 es {es_par_o_impar(4)}") # Debería imprimir "par"
print(f"El número 7 es {es_par_o_impar(7)}") # Debería imprimir "impar"

print("\nProbando Ejercicio 4 (invertir_cadena):")
print(f"La cadena 'hola' invertida es: {invertir_cadena('hola')}") # Debería imprimir "aloh"

print("\nProbando Ejercicio 5 (encontrar_maximo):")
print(f"El número máximo en [1, 5, 2, 8, 3] es: {encontrar_maximo([1, 5, 2, 8, 3])}") # Debería imprimir 8

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
print(f"Hola, {nombre} {apellido}!")

