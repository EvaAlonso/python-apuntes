#diccionario es una colección de pares clave-valor
# Cada clave es única y se utiliza para acceder a su valor asociado.
# Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación.
# las claves pueden ser de cualquier tipo inmutable (cadenas, números, tuplas) y los valores pueden ser de cualquier tipo.
# veamos un ejemplo de cómo crear y manipular un diccionario en Python.
# Crear un diccionario vacío
diccionario_vacio = {}
print(diccionario_vacio)  # Imprime {}
# Crear un diccionario con elementos
diccionario_numeros = {"uno": 1, "dos": 2, "tres": 3}
print(diccionario_numeros)  # Imprime {'uno': 1, 'dos': 2, 'tres': 3}
# Crear un diccionario con diferentes tipos de datos
diccionario_mixto = {"entero": 1, "cadena": "dos", "flotante": 3.0, "booleano": True}
print(diccionario_mixto)  # Imprime {'entero': 1, 'cadena': 'dos', 'flotante': 3.0, 'booleano': True}
# Acceder a un valor por su clave
print(diccionario_numeros["uno"])  # Imprime 1, el valor asociado a la clave "uno"
print(diccionario_numeros["dos"])  # Imprime 2, el valor asociado a la clave "dos"
# Añadir un nuevo par clave-valor al diccionario
diccionario_numeros["cuatro"] = 4
print(diccionario_numeros)  # Imprime {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
# Modificar el valor de una clave existente
diccionario_numeros["dos"] = 22
print(diccionario_numeros)  # Imprime {'uno': 1, 'dos': 22, 'tres': 3, 'cuatro': 4}
# Eliminar un par clave-valor del diccionario
del diccionario_numeros["tres"]  # Elimina la clave "tres" y su valor asociado
print(diccionario_numeros)  # Imprime {'uno': 1, 'dos': 22, 'cuatro': 4}
# Comprobar si una clave está en el diccionario
print("uno" in diccionario_numeros)  # Imprime True, ya que "uno" es una clave en el diccionario
print("cinco" in diccionario_numeros)  # Imprime False, ya que "cinco" no es una clave en el diccionario
# Obtener todas las claves del diccionario
print(diccionario_numeros.keys())  # Imprime dict_keys(['uno', 'dos', 'cuatro'])
# Obtener todos los valores del diccionario
print(diccionario_numeros.values())  # Imprime dict_values([1, 22, 4])
# Obtener todos los pares clave-valor del diccionario
print(diccionario_numeros.items())  # Imprime dict_items([('uno', 1), ('dos', 22), ('cuatro', 4)])
# Longitud del diccionario
print(len(diccionario_numeros))  # Imprime 3, la cantidad de pares clave-valor en el diccionario
# Limpiar el diccionario
diccionario_numeros.clear()  # Elimina todos los pares clave-valor del diccionario
print(diccionario_numeros)  # Imprime {}, el diccionario está vacío
# Recorrer un diccionario con un bucle for
for clave, valor in diccionario_mixto.items():
    print(f"Clave: {clave}, Valor: {valor}")
#métodos de diccionarios
# Los diccionarios tienen varios métodos útiles, como get(), pop(), update() y others
# get(): Obtiene el valor asociado a una clave, devolviendo None si la clave no existe
print(diccionario_mixto.get("cadena"))  # Imprime 'dos', el valor asociado a la clave "cadena"
print(diccionario_mixto.get("inexistente"))  # Imprime None, ya que "inexistente" no es una clave en el diccionario
# pop(): Elimina y devuelve el valor asociado a una clave, devolviendo None si la clave no existe
valor_eliminado = diccionario_mixto.pop("flotante", None)
print(valor_eliminado)  # Imprime 3.0, el valor eliminado
print(diccionario_mixto)  # Imprime {'entero': 1, 'cadena': 'dos', 'booleano': True}
# update(): Actualiza el diccionario con los pares clave-valor de otro diccionario
diccionario_mixto.update({"nuevo": "valor", "booleano": False})
print(diccionario_mixto)  # Imprime {'entero': 1, 'cadena': 'dos', 'booleano': False, 'nuevo': 'valor'}
#veamos como añadir, modificar y eliminar elementos en un diccionario
diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
# Añadir un nuevo par clave-valor
diccionario["profesión"] = "Ingeniera"
print(diccionario)  # Imprime {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid', 'profesión': 'Ingeniera'}
# Modificar el valor de una clave existente
diccionario["edad"] = 26
print(diccionario)  # Imprime {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid', 'profesión': 'Ingeniera'}
# Eliminar un par clave-valor
del diccionario["ciudad"]  # Elimina la clave "ciudad" y su valor asociado
print(diccionario)  # Imprime {'nombre': 'Ana', 'edad': 26, 'profesión': 'Ingeniera'}
# Comprobar si una clave está en el diccionario
print("nombre" in diccionario)  # Imprime True, ya que "nombre"
# es una clave en el diccionario
print("ciudad" in diccionario)  # Imprime False, ya que "ciudad" no es una clave en el diccionario

# para ver más sobre diccionarios en la documentación oficial de Python, visita https://docs.python.org/3/tutorial/datastructures.html#dictionaries