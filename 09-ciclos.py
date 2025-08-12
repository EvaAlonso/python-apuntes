# Un ciclo nos permite repetir un bloque de código varias veces. son una estructura de control fundamental en la programación.
# En Python, los ciclos más comunes son el ciclo for y el ciclo while.
# Ciclo for: Repite un bloque de código para cada elemento en una secuencia (como una lista, tupla o cadena).
# Ejemplo de ciclo for
numeros = [1, 2, 3, 4, 5] 
for numero in numeros:  # Itera sobre cada elemento en la lista numeros
    print(numero)  # Imprime el número actual en cada iteración
# Ciclo while: Repite un bloque de código mientras una condición sea verdadera.
# Ejemplo de ciclo while
contador = 0  # Inicializa el contador en 0
while contador < 5:  # Mientras el contador sea menor que 5
    print(contador)  # Imprime el valor actual del contador
    contador += 1  # Incrementa el contador en 1 en cada iteración
# Ciclos anidados: Un ciclo dentro de otro ciclo
for i in range(3):  # Itera 3 veces
    for j in range(2):  # Itera 2 veces dentro del ciclo anterior
        print(f"i: {i}, j: {j}")  # Imprime los valores de i y j en cada iteración
        
# Uso de la función range() para generar una secuencia de números
for i in range(5):  # Itera desde 0 hasta 4
    print(i)  # Imprime el valor de i en cada iteración
# Uso de la función range() con un paso específico
for i in range(0, 10, 2):  # Itera desde 0 hasta 9 con un paso de 2
    print(i)  # Imprime los números pares del 0 al 8
    
# Uso de la función range() con números negativos
for i in range(5, 0, -1):  # Itera desde 5 hasta 1 en decrementos de 1
    print(i)  # Imprime los números del 5 al 1 en orden descendente
# Uso de la función range() con un solo argumento
for i in range(3):  # Itera desde 0 hasta 2
    print(i)  # Imprime el valor de i en cada iteración
# Uso de la función range() con un rango específico
for i in range(1, 6):  # Itera desde 1 hasta 5
    print(i)  # Imprime el valor de i en cada iteración
# Uso de la función range() con un rango específico y un paso
for i in range(1, 10, 3):  # Itera desde 1 hasta 9 con un paso de 3
    print(i)  # Imprime los números 1, 4, 7, 10
    
# Ciclos sobre iterables: Puedes usar ciclos for para iterar sobre cualquier objeto iterable, como cadenas, listas, tuplas, diccionarios, etc.
cadena = "Hola"
for letra in cadena:  # Itera sobre cada carácter en la cadena
    print(letra)  # Imprime cada letra de la cadena
# Ciclos con listas: Puedes usar ciclos for para iterar sobre listas y realizar operaciones en cada elemento.
lista = [10, 20, 30, 40]
for numero in lista:  # Itera sobre cada elemento en la lista
    print(numero)  # Imprime cada número de la lista
# Ciclos con diccionarios: Puedes iterar sobre las claves o los valores de un diccionario.
diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():  # Itera sobre las claves y valores del diccionario
    print(f"Clave: {clave}, Valor: {valor}")  # Imprime cada clave y su valor asociado
# Uso de la función enumerate() para obtener el índice y el valor al mismo tiempo
for indice, valor in enumerate(lista):  # Itera sobre la lista con el índice y el valor
    print(f"Índice: {indice}, Valor: {valor}")  # Imprime el índice y el valor correspondiente
    
# Ciclos while con condiciones: Puedes usar ciclos while para repetir un bloque de código mientras una condición sea verdadera.
numero = 0  # Inicializa el número en 0
while numero < 5:  # Mientras el número sea menor que 5
    print(numero)  # Imprime el valor actual del número
    numero += 1  # Incrementa el número en 1 en cada iteración
diccionario["edad"] = 26
print(diccionario)  # Imprime {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid', 'profesión': 'Ingeniera'}
    
# Para saber más sobre ciclos en Python, puedes consultar la documentación oficial en https://docs.python.org/3/tutorial/controlflow.html#for-statements
