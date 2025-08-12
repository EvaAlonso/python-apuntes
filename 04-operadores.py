#Operadores son símbolos que denotan una operación en el programa. 
#Operandos son los valores sobre los que se realiza la operación.
# operador + operando = expresión
# Una expresión es una combinación de valores, variables y operadores que al ser evaluados resultan en un valor.
# Suma
print(2 + 2)  # 4

# Resta
print(4 - 2)  # 2

# Multiplicación
print(4 * 2)  # 8

# División
print(2/4)  # 0.5
# División por cero no está definida y generará un error.

# Otras operaciones
# Potencia
print(2 ** 3)  # 8
# División sin decimal, división entera
print(5//4)  # 1

# Modulo (lo que sobra de la división: Residuo)
print(6 % 4)  # 2

# Redondear : round()
print(round(3.1))  # 3
print(round(3.9))  # 4

# Valor absoluto : abs()
print(abs(-20))

#Operadores de comparación comparan valores y devuelven un valor booleano (True o False).
# Igualdad
print(2 == 2)  # True
# Desigualdad
print(2 != 3)  # True
# Mayor que
print(3 > 2)  # True
# Menor que
print(2 < 3)  # True
# Mayor o igual que
print(3 >= 3)  # True
# Menor o igual que
print(2 <= 3)  # True

# Operadores lógicos
# AND: Verdadero si ambos operandos son verdaderos
print(True and True)  # True
# OR: Verdadero si al menos uno de los operandos es verdadero
print(True or False)  # True
# NOT: Invierte el valor lógico del operando
print(not True)  # False
# Operadores de identidad
# is: Verifica si dos variables apuntan al mismo objeto
a = [1, 2, 3]
b = a
print(a is b)  # True, ya que a y b apuntan al mismo objeto
# is not: Verifica si dos variables no apuntan al mismo objeto
print(a is not b)  # False, ya que a y b apuntan al mismo objeto
# Operadores de pertenencia
# in: Verifica si un elemento está en una colección (lista, tupla, cadena, etc.)
print(2 in [1, 2, 3])  # True, ya que 2 está en la lista
# not in: Verifica si un elemento no está en una colección  
print(4 not in [1, 2, 3])  # True, ya que 4 no está en la lista
# Operadores de asignación
# Asignación simple
x = 5  # Asigna el valor 5 a la variable x
# Asignación con suma
x += 2  # Equivalente a x = x + 2, ahora x es 7
# Asignación con resta
x -= 3  # Equivalente a x = x - 3, ahora x es 4
# Asignación con multiplicación
x *= 2  # Equivalente a x = x * 2, ahora x es 8
# Asignación con división
x /= 4  # Equivalente a x = x / 4, ahora x es 2.0
# Asignación con potencia
x **= 3  # Equivalente a x = x ** 3, ahora x es 8.0
# Asignación con división entera
x //= 2  # Equivalente a x = x // 2, ahora x es 4.0
# Asignación con módulo
x %= 3  # Equivalente a x = x % 3, ahora x es 1.0
# Asignación con concatenación de cadenas 
cadena = "Hola"
cadena += " Mundo"  # Equivalente a cadena = cadena + " Mundo", ahora cadena es "Hola Mundo"
# Asignación con repetición de cadenas
cadena *= 2  # Equivalente a cadena = cadena * 2, ahora cadena es "Hola MundoHola Mundo"
print(cadena)  # Imprime "Hola MundoHola Mundo"
# Asignación con listas
lista = [1, 2, 3]
lista += [4, 5]  # Equivalente a lista = lista + [4, 5], ahora lista es [1, 2, 3, 4, 5]
print(lista)  # Imprime [1, 2, 3, 4, 5] 
# Asignación con tuplas
tupla = (1, 2, 3)
tupla += (4, 5)  # Equivalente a tupla = tupla + (4, 5), ahora tupla es (1, 2, 3, 4, 5)
print(tupla)  # Imprime (1, 2, 3, 4, 5)
# Asignación con diccionarios 
diccionario = {"a": 1, "b": 2}
diccionario["c"] = 3  # Asigna el valor 3 a la clave "c", ahora diccionario es {"a": 1, "b": 2, "c": 3}
print(diccionario)  # Imprime {"a": 1, "b": 2, "c": 3}
# Asignación con conjuntos
conjunto = {1, 2, 3}
conjunto.add(4)  # Agrega el elemento 4 al conjunto, ahora conjunto es {1, 2, 3, 4}
print(conjunto)  # Imprime {1, 2, 3, 4}
