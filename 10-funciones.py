# Funciones en python son una forma de agrupar código que realiza una tarea específica.
# Permiten reutilizar código y organizarlo de manera más clara.
# Definición de una función simple
def saludar():  # Define una función llamada saludar
    print("¡Hola, mundo!")  # Imprime un saludo al llamar a la función
# Llamada a la función
saludar()  # Llama a la función saludar, lo que ejecuta el código
# Funciones con parámetros
def saludar_persona(nombre):  # Define una función que recibe un parámetro nombre
    print(f"¡Hola, {nombre}!")  # Imprime un saludo personalizado usando el parámetro
# Llamada a la función con un argumento
saludar_persona("Ana")  # Llama a la función saludar_persona con el argumento "Ana"
# Funciones con retorno de valor
def sumar(a, b):  # Define una función que recibe dos parámetros a y b
    return a + b  # Retorna la suma de a y b
# Llamada a la función y almacenamiento del resultado
resultado = sumar(3, 5)  # Llama a la función sumar con los argumentos 3 y 5, y almacena el resultado en la variable resultado
print(resultado)  # Imprime el resultado de la suma, que es 8
# Funciones con múltiples parámetros
def multiplicar(a, b, c):  # Define una función que recibe tres parámetros a, b y c
    return a * b * c  # Retorna el producto de a, b y c
# diferencia entre argumentos y parámetros
resultado_multiplicacion = multiplicar(2, 3, 4)  # Llama a la función multiplicar con los argumentos 2, 3 y 4, y almacena el resultado en la variable resultado_multiplicacion
print(resultado_multiplicacion)  # Imprime el resultado de la multiplicación, que es 24
# Funciones con parámetros por defecto
def saludar_con_prefijo(nombre, prefijo="Hola"):  # Define una función con un parámetro por defecto
    print(f"{prefijo}, {nombre}!")  # Imprime un saludo personalizado usando el prefijo y el nombre
# Llamada a la función con el parámetro por defecto
saludar_con_prefijo("Carlos")  # Llama a la función sin especificar el prefijo, usa el valor por defecto "Hola"
# Llamada a la función con un prefijo personalizado
saludar_con_prefijo("Ana", "Buenos días")  # Llama a la función especificando un prefijo personalizado

#scope de las funciones
def funcion_externa():
    variable_externa = "Soy una variable externa"  # Variable definida en el ámbito de la función externa
    def funcion_interna():  # Define una función interna
        print(variable_externa)  # Accede a la variable externa desde la función interna
    funcion_interna()  # Llama a la función interna 
# Llamada a la función externa, lo que ejecuta la función interna
funcion_externa()  # Llama a la función externa, lo que imprime "Soy una variable externa"
# Funciones anónimas (lambda)
# Las funciones lambda son funciones pequeñas y anónimas que se definen en una sola línea
suma = lambda x, y: x + y  # Define una función lambda que suma dos números
print(suma(3, 5))  # Llama a la función lambda con los argumentos 3 y 5, e imprime el resultado, que es 8

