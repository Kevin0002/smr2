print("Hola Mundo")  # La función print muestra texto en la consola

# Tipos de variables
entero = 10  # Variable de tipo entero
flotante = 3.14  # Variable de tipo flotante
cadena = "Hola"  # Variable de tipo cadena
booleano = True  # Variable de tipo booleano

# Operaciones básicas
suma = entero + 5  # Suma
resta = flotante - 1.14  # Resta
multiplicacion = entero * 2  # Multiplicación
potencia = entero**2  # Potencia
division = flotante / 2  # División
Division_entera = entero // 3  # División entera
modulo = entero % 3  # Módulo

# Operadores de nivel de bit
and_bit = entero & 3  # Operador AND a nivel de bit
or_bit = entero | 2  # Operador OR a nivel de bit
xor_bit = entero ^ 1  # Operador XOR a nivel de bit
desplazamiento_izquierda = entero << 1  # Desplazamiento a la izquierda
desplazamiento_derecha = entero >> 1  # Desplazamiento a la derecha
not_bit = ~entero  # Operador NOT a nivel de bit

# Booleanos
and_logico = booleano and False  # Operador AND lógico
or_logico = booleano or False  # Operador OR lógico
not_logico = not booleano  # Operador NOT lógico

# Comparaciones
igual = entero == 10  # Igualdad
diferente = flotante != 3.14  # Desigualdad
mayor_que = entero > 5  # Mayor que
menor_que = flotante < 4.0  # Menor que
mayor_igual = entero >= 10  # Mayor o igual que
menor_igual = flotante <= 3.14  # Menor o igual que

# Listas
mi_lista = [1, 2, 3, 4, 5]  # Definición de una lista
mi_lista.append(6)  # Agregar un elemento al final de la lista
primer_elemento = mi_lista[0]  # Acceder al primer elemento
longitud_lista = len(mi_lista)  # Obtener la longitud de la lista
mi_lista.remove(3)  # Eliminar el elemento con valor 3

# Tuplas
mi_tupla = (1, 2, 3)  # Definición de una tupla
primer_elemento_tupla = mi_tupla[0]  # Acceder al primer elemento de la tupla
longitud_tupla = len(mi_tupla)  # Obtener la longitud de la tupla

# Diccionarios
mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
}  # Definición de un diccionario
valor_clave1 = mi_diccionario["clave1"]  # Acceder al valor de "clave1"
mi_diccionario["clave3"] = "valor3"  # Agregar un nuevo par clave-valor
del mi_diccionario["clave2"]  # Eliminar el par clave-valor con clave "clave2"


# Sentencias condicionales y bucles

# if-else
if entero > 5:  # Condicional if
    print("El número es mayor que 5")  # Acción si la condición es verdadera
else:  # Bloque else
    print("El número es 5 o menor")  # Acción si la condición es falsa

# Bucle for
for i in range(5):  # Bucle for que itera de 0 a 4
    print("Iteración número:", i)  # Muestra el número de iteración

# Bicle while
contador = 0  # Inicialización del contador
while contador < 3:  # Bucle while que se ejecuta mientras el contador sea menor que 3
    print("Contador:", contador)  # Muestra el valor del contador
    contador += 1  # Incrementa el contador en 1


# Definición de función
def saludar(nombre):  # Definición de la función saludar
    return "Hola, " + nombre  # Retorna un saludo personalizado


print(saludar("Mundo"))  # Llama a la función saludar y muestra el resultado

