saludo = "Hola, mundo!"
print(saludo)

#Para ejecutar este script, utiliza el comando:
# python 01-variables-tipos-datos.py en consola o terminal.

#Variable: Nombre que se le asigna aun valor en el programa. Ese nombre representa un espacio en memoria donde se almacena el valor.
# = es el operador de asignación, que asigna un valor a una variable.
#Tipo de dato: Clasificación de los valores en Python, como enteros, flotantes, cadenas, etc.
# Reglas para nombrar variables:
# - Deben comenzar con una letra (a-z, A-Z) o un guion bajo (_) el guión bajo normalmente no se usa al principio.
# - Pueden contener letras, números (0-9) y guiones bajos (_).
# - No pueden comenzar con un número. Te dará error de sintaxis.
# - Resumen: Valores alfanumérios (A-Z, a-z, 0-9, _), el guión bajo (_) se usa para separar palabras en nombres de variables.
# - Se distinguen entre mayúsculas y minúsculas, por lo que "variable" y "Variable" son diferentes.


# Tipos de datos en Python
# Entero (int): Números enteros, positivos o negativos y el cero(es positivo).
# Para averiguar el tipo de dato de una variable, se puede usar la función type().
print(type(saludo))  # Esto imprimirá <class 'str'>, indicando que saludo es una cadena de texto.
numero_entero = 42
print(numero_entero)
# Flotante (float): Números con decimales.
numero_flotante = 3.14
print(numero_flotante)
# Cadena (str): Texto, encerrado entre comillas simples o dobles.Secuencia de caracteres encerrados entre comillas simples (' ') o dobles (" ").
cadena_texto = "¡Hola, Python!"
print(cadena_texto)
# Booleano (bool): Verdadero o falso, representado por True o False.
booleano = True
print(booleano)
# Lista (list): Colección ordenada de elementos, que pueden ser de diferentes tipos.
lista = [1, 2, 3, "cuatro", 5.0]
print(lista)
# Tupla (tuple): Similar a una lista, pero inmutable (no se puede modificar).
tupla = (1, 2, 3, "cuatro", 5.0)
print(tupla)
# Diccionario (dict): Colección de pares clave-valor, donde cada clave es única.
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(diccionario)
# Conjunto (set): Colección no ordenada de elementos únicos.
conjunto = {1, 2, 3, 4, 5}
print(conjunto)
# None: Representa la ausencia de valor o un valor nulo.
valor_nulo = None
print(valor_nulo)
# Comentario: Este es un comentario en Python, no afecta la ejecución del código.
