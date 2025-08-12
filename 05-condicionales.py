#Sentencias condicionales
# Condicionales simples
numero = 10
if numero > 5:  # Si el número es mayor que 5
    print("El número es mayor que 5")  # Imprime si la condición es verdadera
    
# Condicionales compuestos
if numero > 5:  # Si el número es mayor que 5
    print("El número es mayor que 5")  # Imprime si la condición es verdadera
else:  # Si la condición anterior es falsa
    print("El número no es mayor que 5")
    
# Condicionales anidados
if numero > 5:  # Si el número es mayor que 5
    print("El número es mayor que 5")  # Imprime si la condición es verdadera
    if numero > 10:  # Si el número es mayor que 10
        print("El número es mayor que 10")  # Imprime si la condición es verdadera
    else:  # Si la condición anterior es falsa
        print("El número no es mayor que 10")

# Condicionales múltiples else if de javascript se simplifica a elif en Python
if numero > 10:  # Si el número es mayor que 10 
    print("El número es mayor que 10")  # Imprime si la condición es verdadera
elif numero > 5:  # Si el número es mayor que 5 pero no mayor que 10
    print("El número es mayor que 5 pero no mayor que 10")  # Imprime si la condición es verdadera
else:  # Si ninguna de las condiciones anteriores es verdadera  
    print("El número no es mayor que 5")

# Condicionales con operadores lógicos
if numero > 5 and numero < 15:  # Si el número es mayor que 5 y menor que 15
    print("El número está entre 5 y 15")  # Imprime si ambas condiciones son verdaderas
if numero < 5 or numero > 15:  # Si el número es menor que 5 o mayor que 15
    print("El número es menor que 5 o mayor que 15")  # Imprime si al menos una condición es verdadera

# Condicionales con operadores de pertenencia
lista = [1, 2, 3, 4, 5]
if numero in lista:  # Si el número está en la lista
    print("El número está en la lista")  # Imprime si la condición es verdadera
if numero not in lista:  # Si el número no está en la lista
    print("El número no está en la lista")  # Imprime si la condición es verdadera

# Condicionales con operadores de identidad
a = [1, 2, 3]
b = a  # b es una referencia al mismo objeto que a
if a is b:  # Si a y b son el mismo objeto
    print("a y b son el mismo objeto")  # Imprime si la condición es verdadera
if a is not b:  # Si a y b no son el mismo objeto
    print("a y b no son el mismo objeto")  # Imprime si la condición es verdadera

# Condicionales con operadores de comparación
if numero == 10:  # Si el número es igual a 10
    print("El número es igual a 10")  # Imprime si la condición es verdadera
if numero != 10:  # Si el número no es igual a 10
    print("El número no es igual a 10")  # Imprime si la condición es verdadera
    