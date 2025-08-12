# Recursión es definir algo en términos de sí mismo

# Ejemplo clásico: calcular el factorial de un número usando recursión

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

# Prueba de la función
print(factorial(5))  # Salida: 120

# Ejemplo de recursión con la sucesión de Fibonacci
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
  
# Prueba de la función
print(fibonacci(6))  # Salida: 8

# Ejemplo de recursión para sumar los números de una lista
def suma_lista(lista):
  if not lista:  # Caso base: si la lista está vacía
    return 0
  else:
    return lista[0] + suma_lista(lista[1:])  # Suma el primer elemento con la suma del resto de la lista  
# Prueba de la función
print(suma_lista([1, 2, 3, 4, 5]))  # Salida: 15

# Ejemplo de recursión para invertir una cadena
def invertir_cadena(cadena):
  if len(cadena) == 0:  # Caso base: si la cadena está vacía
    return ""
  else:
    return cadena[-1] + invertir_cadena(cadena[:-1])  # Añade el último carácter al resultado de invertir el resto de la cadena 
# Prueba de la función
print(invertir_cadena("hola"))  # Salida: "aloh"

# Ejemplo de recursión para encontrar el máximo en una lista
def maximo_lista(lista):
  if len(lista) == 1:  # Caso base: si la lista tiene un solo elemento
    return lista[0]
  else:
    max_resto = maximo_lista(lista[1:])  # Encuentra el máximo del resto de la lista
    return max(lista[0], max_resto)  # Compara el primer elemento con el máximo del resto
# Prueba de la función
print(maximo_lista([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Salida: 9

# Las funciones recursivas deben de tener un caso base y un caso recursivo
#El caso base permite que la recursión se detenga(llamarse a sí misma)
# caso recursivo es el que nos permite dividir el problema en uno más pequeño que se llame a sí mismo
#hasta llebar al caso base que detiene el proceso