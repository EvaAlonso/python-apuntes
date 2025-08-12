# Cadena (str): Texto, encerrado entre comillas simples o dobles.Secuencia de caracteres encerrados entre comillas simples (' ') o dobles (" ").
cadena_texto = "¡Hola, Python!"
print(cadena_texto)

# Ojo!! no puedes mezclar comillas simples y dobles en una misma cadena sin escaparlas.
# Recuerda 5 distinto de "5" uno es un entero y el otro es una cadena de texto.
# Tamaño de una cadena de caracteres nos indica cuántos caracteres tiene. y se obtiene con la función len().
print(len(cadena_texto))  # Esto imprimirá 13, que es el número de caracteres en la cadena.
print(len(""))  # Esto imprimirá 0, ya que la cadena está vacía.
# Concatenación: Unir dos o más cadenas de texto.
cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2
print(cadena_concatenada)  # Esto imprimirá "Hola Mundo"
# Repetición: Repetir una cadena varias veces.
cadena_repetida = cadena1 * 3
print(cadena_repetida)  # Esto imprimirá "HolaHolaHola"

# Subcadenas: Extraer partes de una cadena.
subcadena = cadena_texto[0:5]  # Extrae los primeros 5 caracteres
print(subcadena)  # Esto imprimirá "¡Hola"

# Acceso a caracteres: Puedes acceder a un carácter específico de una cadena usando su índice.
caracter = cadena_texto[0]  # Accede al primer carácter
print(caracter)  # Esto imprimirá "¡"

# Formateo de cadenas: Insertar valores en una cadena.
nombre = "Juan" 
edad = 30
cadena_formateada = f"Mi nombre es {nombre} y tengo {edad} años."
print(cadena_formateada)  # Esto imprimirá "Mi nombre es Juan y tengo 30 años."

# Rebanado o slicing: Extraer una parte de la cadena.
cadena_slicing = cadena_texto[0:5]  # Extrae los primeros 5 caracteres
print(cadena_slicing)  # Esto imprimirá "¡Hola" 
# empieza en el índice 0 y termina antes del índice 5. cadena[inicio:fin]
#cadena_texto[7:]  # Extrae desde el índice 7 hasta el final
# cadena_texto[:5]  # Extrae desde el inicio hasta el índice 5 (sin incluirlo)
# cadena_texto[-1]  # Accede al último carácter de la cadena
# cadena_texto[:]
# ¿Cómo poner mi nombre al revés?

name = "Ricardo"
print(name)
name_reverse = name[::-1]
print(name_reverse)
print(name[0:3:2])  # Extrae caracteres desde el índice 0 al 3, saltando de 2 en 2
nombre = "José"
# no estoy mutando estoy reasignando el valor variable
name = "Ricardo"
name[0] = "L"
# Da error no podemos mutar

# Métodos de cadenas: Python ofrece muchos métodos para trabajar con cadenas.
# Métodos son operaciones comunes (funciones) que vienen implementadas en Python.
# cadena.método(valores)
# Por ejemplo, convertir a mayúsculas o minúsculas.
cadena_mayusculas = cadena_texto.upper()  # Convierte a mayúsculas
print(cadena_mayusculas)  # Esto imprimirá "¡HOLA, PYTHON!"
cadena_minusculas = cadena_texto.lower()  # Convierte a minúsculas
print(cadena_minusculas)  # Esto imprimirá "¡hola, python!"
cadena_titulo = cadena_texto.title()  # Convierte a título (primera letra de cada palabra en mayúscula)
print(cadena_titulo)  # Esto imprimirá "¡Hola, Python!"
# Reemplazar texto en una cadena.
cadena_reemplazada = cadena_texto.replace("Python", "Mundo")  # Reemplaza "Python" por "Mundo"
print(cadena_reemplazada)  # Esto imprimirá "¡Hola, Mundo!"
# capitalizar la primera letra de la cadena.
cadena_capitalizada = cadena_texto.capitalize()  # Capitaliza la primera letra
print(cadena_capitalizada)  # Esto imprimirá "¡Hola, python!"

# find: Buscar una subcadena dentro de una cadena.
posicion = cadena_texto.find("Python")  # Encuentra la posición de "Python"
print(posicion)  # Esto imprimirá 6, que es la posición de "Python" en la cadena.
# split: Dividir una cadena en una lista de subcadenas.
lista_palabras = cadena_texto.split(", ")  # Divide la cadena en una lista usando ", " como separador
print(lista_palabras)  # Esto imprimirá ['¡Hola', 'Python!']
# join: Unir una lista de cadenas en una sola cadena.
lista = ["Hola", "Python"]
cadena_unida = " ".join(lista)  # Une la lista en una cadena separada por espacios
print(cadena_unida)  # Esto imprimirá "Hola Python"
# strip: Eliminar espacios en blanco al inicio y al final de una cadena.
cadena_con_espacios = "   Hola, Python!   "
cadena_sin_espacios = cadena_con_espacios.strip()  # Elimina espacios
print(cadena_sin_espacios)  # Esto imprimirá "Hola, Python!" sin espacios al inicio y al final.
# count: Contar cuántas veces aparece una subcadena en una cadena.
contador = cadena_texto.count("o")  # Cuenta cuántas veces aparece "o"
print(contador)  # Esto imprimirá 2, ya que "o" aparece dos veces en la cadena.
# isdigit: Verifica si todos los caracteres de la cadena son dígitos.
cadena_numerica = "12345"
print(cadena_numerica.isdigit())  # Esto imprimirá True, ya que todos los caracteres son dígitos.
# isalpha: Verifica si todos los caracteres de la cadena son letras.
cadena_letras = "Hola"
print(cadena_letras.isalpha())  # Esto imprimirá True, ya que todos los caracteres son letras.
# isalnum: Verifica si todos los caracteres de la cadena son alfanuméricos (letras o dígitos).
cadena_alfanumerica = "Hola123"
print(cadena_alfanumerica.isalnum())  # Esto imprimirá True,
# ya que todos los caracteres son letras o dígitos.
# isspace: Verifica si todos los caracteres de la cadena son espacios en blanco.
cadena_espacios = "   "
print(cadena_espacios.isspace())  # Esto imprimirá True, ya que todos los caracteres son espacios en blanco.
# startswith: Verifica si una cadena comienza con una subcadena específica.
print(cadena_texto.startswith("¡Hola"))  # Esto imprimirá True, ya que la cadena comienza con "¡Hola".
# endswith: Verifica si una cadena termina con una subcadena específica.  
print(cadena_texto.endswith("Python!"))  # Esto imprimirá True, ya que la cadena termina con "Python!".
# splitlines: Divide una cadena en líneas, útil para cadenas multilínea.
cadena_multilinea = "Línea 1\nLínea 2\nLínea 3"
lineas = cadena_multilinea.splitlines()  # Divide la cadena en líneas
print(lineas)  # Esto imprimirá ['Línea 1', 'Línea 2', 'Línea 3']
# index: Similar a find, pero lanza un error si la subcadena no se encuentra.
try:
    posicion_index = cadena_texto.index("Python")  # Encuentra la posición de "Python"
    print(posicion_index)  # Esto imprimirá 6, que es la posición de "Python" en la cadena.
except ValueError:
    print("Subcadena no encontrada")
# islower: Verifica si todos los caracteres de la cadena están en minúsculas.
print(cadena_texto.islower())  # Esto imprimirá False, ya que la cadena tiene mayúsculas.
# isupper: Verifica si todos los caracteres de la cadena están en mayúsculas.
print(cadena_texto.isupper())  # Esto imprimirá False, ya que la cadena tiene minúsculas.
# zfill: Rellena una cadena con ceros a la izquierda hasta alcanzar una longitud específica.
cadena_numero = "42"
cadena_zfill = cadena_numero.zfill(5)  # Rellena con ceros a la izquierda hasta 5 caracteres
print(cadena_zfill)  # Esto imprimirá "00042", que es la cadena original con ceros a la izquierda.

# ver más métodos de cadenas en la documentación oficial de Python:
# https://docs.python.org/3/library/stdtypes.html#string-methods

