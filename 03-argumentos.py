# Para recibir datos del usuario, se utiliza la función input().
# Esta función detiene la ejecución del programa y espera a que el usuario ingrese un valor.
# El valor ingresado se almacena en una variable.
#LA FUNCIÓN INPUT() SIEMPRE DEVUELVE UNA CADENA DE CARACTERES.
nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre_usuario}!")  # Imprime un saludo personalizado con el nombre ingresado por el usuario.
# Argumentos: Son valores que se pasan a una función cuando se llama.
# En este caso, el argumento es el texto que se muestra al usuario.
# La función input() toma un argumento que es el mensaje que se muestra al usuario.
# Ejemplo de uso de input() para recibir un número y realizar una operación.
numero = input("Por favor, ingresa un número: ")
# El valor ingresado es una cadena de texto, por lo que si se quiere realizar una operación matemática, es necesario convertirlo a un tipo numérico.
numero = int(numero)  # Convierte la cadena a un entero.
resultado = numero * 2  # Multiplica el número ingresado por 2.
print(f"El doble de {numero} es {resultado}.")  # Imprime el resultado de la operación.
# Recuerda que input() siempre devuelve una cadena de texto, por lo que es importante convertir el valor a un tipo adecuado si se va a realizar una operación matemática.
# Ejemplo de uso de input() para recibir un número decimal.
numero_decimal = input("Por favor, ingresa un número decimal: ")
numero_decimal = float(numero_decimal)  # Convierte la cadena a un número decimal.
resultado_decimal = numero_decimal / 2  # Divide el número ingresado por 2.
print(f"La mitad de {numero_decimal} es {resultado_decimal}.")  # Imprime el resultado de la operación.
# Es importante validar la entrada del usuario para evitar errores si se ingresa un valor no numérico.
# Ejemplo de validación de entrada del usuario.
try:
    numero_valido = input("Por favor, ingresa un número entero: ")
    numero_valido = int(numero_valido)  # Intenta convertir la entrada a un entero.
    print(f"El número ingresado es {numero_valido}.") # Imprime el número ingresado.
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
# En este ejemplo, si el usuario ingresa un valor no numérico, se captura la excepción ValueError y se muestra un mensaje de error.
# Recuerda que input() es una función que permite interactuar con el usuario, y los argumentos son valores que se pasan a las funciones para personalizar su comportamiento.
# Ejemplo de uso de input() para recibir una cadena de texto y realizar una operación.
cadena_usuario = input("Por favor, ingresa una cadena de texto: ")
# En este caso, la cadena ingresada se almacena en la variable cadena_usuario.
# Puedes realizar operaciones con la cadena, como calcular su longitud o convertirla a mayúsculas.
longitud_cadena = len(cadena_usuario)  # Calcula la longitud de la cadena 