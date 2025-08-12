#listas en pythnon
# Las listas son colecciones ordenadas y mutables de elementos.
# Se definen utilizando corchetes [] y pueden contener elementos de diferentes tipos.
# Crear una lista vacía
lista_vacia = []
print(lista_vacia)  # Imprime []
# Crear una lista con elementos
lista_numeros = [1, 2, 3, 4, 5]
print(lista_numeros)  # Imprime [1, 2, 3, 4, 5]
# Crear una lista con diferentes tipos de datos
lista_mixta = [1, "dos", 3.0, True] # Imprime [1, 'dos', 3.0, True]
# Acceder a elementos de una lista por su índice
print(lista_numeros[0])  # Imprime 1, el primer elemento de la lista
print(lista_numeros[2])  # Imprime 3, el tercer elemento de la lista
# Acceder al último elemento de la lista
print(lista_numeros[-1])  # Imprime 5, el último elemento de la lista
# Acceder a un rango de elementos (rebanado o slicing)
print(lista_numeros[1:4])  # Imprime [2, 3, 4], los elementos desde el índice 1 hasta el 3 (sin incluir el 4)
# Modificar un elemento de la lista
lista_numeros[0] = 10  # Cambia el primer elemento de la lista a 10
print(lista_numeros)  # Imprime [10, 2, 3, 4, 5]
# Añadir elementos a la lista
lista_numeros.append(6)  # Añade el número 6 al final de la lista
print(lista_numeros)  # Imprime [10, 2, 3, 4, 5, 6]
# Insertar un elemento en una posición específica
lista_numeros.insert(1, 20)  # Inserta el número 20 en la posición 1
print(lista_numeros)  # Imprime [10, 20, 2, 3, 4, 5, 6]
# Eliminar un elemento de la lista por su valor
lista_numeros.remove(20)  # Elimina el número 20 de la lista
print(lista_numeros)  # Imprime [10, 2, 3, 4, 5, 6]
# Eliminar un elemento de la lista por su índice
del lista_numeros[0]  # Elimina el primer elemento de la lista
print(lista_numeros)  # Imprime [2, 3, 4, 5, 6]
# Eliminar el último elemento de la lista
ultimo_elemento = lista_numeros.pop()  # Elimina y devuelve el último elemento
print(ultimo_elemento)  # Imprime 6, el último elemento eliminado
print(lista_numeros)  # Imprime [2, 3, 4, 5]
# Longitud de la lista
print(len(lista_numeros))  # Imprime 4, la cantidad de elementos en la lista
# Ordenar la lista
lista_numeros.sort()  # Ordena la lista en orden ascendente
print(lista_numeros)  # Imprime [2, 3, 4, 5]
# Invertir el orden de la lista
lista_numeros.reverse()  # Invierte el orden de los elementos en la lista
print(lista_numeros)  # Imprime [5, 4, 3, 2]
# Comprobar si un elemento está en la lista 
print(3 in lista_numeros)  # Imprime True, ya que 3 está en la lista
print(10 in lista_numeros)  # Imprime False, ya que 10 no está en la lista
# Limpiar la lista
lista_numeros.clear()  # Elimina todos los elementos de la lista
print(lista_numeros)  # Imprime [], la lista está vacía
# Listas anidadas: Listas dentro de listas
lista_anidada = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(lista_anidada)  # Imprime [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
# Acceder a un elemento de una lista anidada
print(lista_anidada[0][1])  # Imprime 2, el segundo elemento de la primera lista anidada
# Recorrer una lista con un bucle for
for numero in lista_numeros:
    print(numero)  # Imprime cada número en la lista
# Comprobar si una lista está vacía
if not lista_numeros:  # Si la lista está vacía
    print("La lista está vacía")  # Imprime si la lista no tiene elementos
else:
    print("La lista no está vacía") # Imprime si la lista tiene elementos
# Copiar una lista
lista_copia = lista_numeros.copy()  # Crea una copia superficial de la lista
print(lista_copia)  # Imprime la copia de la lista
# Concatenar listas
lista_concatenada = lista_numeros + [7, 8, 9]  # Une dos listas
print(lista_concatenada)  # Imprime [2, 3, 4, 5, 7, 8, 9]
# Repetir una lista 
lista_repetida = lista_numeros * 2  # Repite la lista dos veces
print(lista_repetida)  # Imprime [2, 3, 4, 5, 2, 3, 4, 5]
# Comprobar si una lista es igual a otra
lista_igual = [2, 3, 4, 5]
print(lista_numeros == lista_igual)  # Imprime True, ya que ambas listas son iguales
# Comprobar si dos listas son diferentes  
print(lista_numeros != lista_igual)  # Imprime False, ya que ambas listas son iguales
# Crear una lista con comprensión de listas
lista_comprension = [x * 2 for x in range(5)]  # Crea una lista con los números del 0 al 4 multiplicados por 2
print(lista_comprension)  # Imprime [0, 2, 4, 6, 8]

# Ver más métodos de listas en la documentación oficial de Python:
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists