# Tuplas en python
# Las tuplas son colecciones ordenadas e inmutables de elementos.
# Se definen utilizando paréntesis () y pueden contener elementos de diferentes tipos.
# se diferencias de las listas en que no se pueden modificar una vez creadas.
# Crear una tupla vacía
tupla_vacia = ()
print(tupla_vacia)  # Imprime ()
# Crear una tupla con elementos 
tupla_numeros = (1, 2, 3, 4, 5)
print(tupla_numeros)  # Imprime (1, 2, 3, 4, 5)
# Crear una tupla con diferentes tipos de datos
tupla_mixta = (1, "dos", 3.0, True)  # Imprime (1, 'dos', 3.0, True)
# Acceder a elementos de una tupla por su índice
print(tupla_numeros[0])  # Imprime 1, el primer elemento de la tupla
print(tupla_numeros[2])  # Imprime 3, el tercer elemento de la tupla
# Acceder al último elemento de la tupla
print(tupla_numeros[-1])  # Imprime 5, el último elemento de la tupla
# Acceder a un rango de elementos (rebanado o slicing)
print(tupla_numeros[1:4])  # Imprime (2, 3, 4), los elementos desde el índice 1 hasta el 3 (sin incluir el 4)
# Intentar modificar un elemento de la tupla (esto generará un error)
# tupla_numeros[0] = 10  # Esto generará un error, ya que las tuplas son inmutables
# Añadir elementos a la tupla (esto generará un error)  
# tupla_numeros.append(6)  # Esto generará un error, ya que las tuplas no tienen el método append
# Eliminar un elemento de la tupla (esto generará un error)
# Contar elementos en la tupla
print(tupla_numeros.count(3))  # Imprime 1, ya que el número 3 aparece una vez en la tupla
# Longitud de la tupla
print(len(tupla_numeros))  # Imprime 5, la cantidad de elementos en la tupla

#saber si un elemento está en la tupla
print(3 in tupla_numeros)  # Imprime True, ya que 3 está en la tupla
print(10 in tupla_numeros)  # Imprime False, ya que 10 no está en la tupla
# Métodos de tuplas
# Las tuplas tienen algunos métodos útiles, como count() y index().
print(tupla_numeros.index(3))  # Imprime 2, el índice del primer elemento con valor 3
# Recorrer una tupla con un bucle for
for numero in tupla_numeros:
    print(numero)  # Imprime cada número en la tupla

#para saber más sobre tuplas en la documentación oficial de Python visit https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences