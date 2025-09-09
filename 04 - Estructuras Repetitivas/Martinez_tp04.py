# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea

# for num in range(0,101):
#     print(num)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

# num = int(input("Ingrese un numero entero: "))

# digitos = len(str(num))
# print(digitos)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

# num1 = int(input("Ingrese el primer numero entero: "))
# num2 = int(input("Ingrese el segundo numero entero: "))

# inicio = min(num1, num2)
# final = max(num1, num2)
# suma = 0

# for i in range(inicio + 1, final):
#     suma += i
# print(f"La suma de los numeros enteros comprendidos entre {num1} y {num2} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.

# num = int(input("Ingrese un numero entero (Ingrese 0 para detener): "))
# total = 0

# while num != 0:
#     total += num
#     num = int(input("Ingrese otro numero entero (Ingrese 0 para detener): "))
# print(f"El total acumulado es de: {total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

# import random
# rand_num = random.randint(0,9)

# num = int(input("Adivina un numero aleatorio entre 0 y 9: "))
# cont = 1

# while num != rand_num:
#     cont += 1
#     num = int(input("Fallaste! Intenta de nuevo: "))

# print(f"Felicidades! Acertaste el numero\nNumero de intentos: {cont}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

# for i in range(100, -1, -1):
#     if i % 2 == 0:
#         print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

# num = int(input("Ingresa un numero entero positivo: "))
# suma = 0

# for i in range(0, num + 1):
#     suma += i
# print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# cantidad = 100
# pares = 0
# impares = 0
# negativos = 0
# positivos = 0

# for i in range(cantidad):
#     num = int(input("Ingrese un numero entero: "))
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1
# print(f"Numeros Pares: {pares}\nNumeros Impares: {impares}\nNumeros Negativos: {negativos}\nNumeros Positivos: {positivos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

# cantidad = 100
# suma = 0

# for i in range(cantidad):
#     num = int(input("Ingresa un numero entero: "))
#     suma += num
# promedio = suma / cantidad

# print(f"El promedio de los valores ingresados es de: {promedio}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
#Tuve que averiguar un poco mas sobre len para el bucle

# num = input("Ingresa un numero entero: ")
# invertido = ""

# for i in range(len(num)-1,-1,-1):
#     invertido += num[i]

# print(invertido)
