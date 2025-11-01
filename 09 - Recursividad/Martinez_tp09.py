# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario

# def fact_recursiva(num):
#     if num == 0:
#         return 1
#     else:
#         return num * fact_recursiva(num - 1)
    
# num = int(input("Ingrese un numero positivo: "))

# for i in range(1, num + 1):
#     print(f"El factorial de {i} es: {fact_recursiva(i)}")



# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique.

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# num = int(input("Ingrese la posicion hasta la que desea ver de la serie de Fibonacci: "))

# for i in range(num + 1):
#     print(f"El valor de la posicion {i} en la serie es: {fibonacci(i)}")



# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛∗𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general.

# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     else:
#         return base * potencia(base, exponente - 1)

# base = int(input("Ingrese la base: "))
# exponente = int(input("Ingrese el exponente: "))

# resultado = potencia(base, exponente)
# print(f"{base} elevado a la {exponente} es: {resultado}")



# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
# unos (1), en base 2.


# def decimal_a_binario(num):
#     if num == 0:
#         return ""
#     else:
#         return decimal_a_binario(num // 2) + str(num % 2)

# num = int(input("Ingrese un numero entero positivo: "))

# if num == 0:
#     print("El numero binario es: 0")
# else:
#     print(f"El numero binario es: {decimal_a_binario(num)}")



# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed()

# def palindromo(palabra):
#     if len(palabra) <= 1:
#         return True
    
#     if palabra[0] != palabra[-1]:
#         return False
    
#     return palindromo(palabra[1:-1])

# palabra_usuario = input("Ingrese una palabra sin espacios ni acentos: ").lower()

# if palindromo(palabra_usuario):
#     print("Es un palindromo")
# else:
#     print("No es un palindromo")



# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 

# def suma_digitos(n):
#     if n < 10:
#         return n
    
#     return (n % 10) + suma_digitos(n // 10)

# num = int(input("Ingrese un numero entero positivo: "))
# resultado = suma_digitos(num)
# print(f"La suma de los digitos de {num} es: {resultado}")



# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 

# def contar_bloques(n):
#     if n == 1:
#         return 1
    
#     return n + contar_bloques(n - 1)

# nivel_bajo = int(input("Ingrese la cantidad de bloques del nivel mas bajo: "))
# total = contar_bloques(nivel_bajo)
# print(f"El total de bloques necesarios es de: {total}")



# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número

# def contar_digito(num, digito):
#     if num == 0:
#         return 0
    
#     if num % 10 == digito:
#         return 1 + contar_digito(num // 10, digito)
#     else:
#         return contar_digito(num // 10, digito)

# num = int(input("Ingrese un numero entero positivo: "))
# digito = int(input("Ingrese un digito entre 0 y 9: "))

# resultado = contar_digito(num, digito)
# print(f"El digito {digito} aparece {resultado} veces en el numero {num}")
