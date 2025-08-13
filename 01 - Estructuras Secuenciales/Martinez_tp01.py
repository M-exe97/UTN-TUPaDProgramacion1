# 1) Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!"
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa "Marcos", el programa debe imprimir
# por pantalla "Hola Marcos!". Consejo: Esto sera mas sencillo si utilizas print(f...) para
# realizar la impresion por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
recidencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {recidencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro
radio = int(input("Ingrese el radio del circulo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El area del circulo es de: {area}. Y su perimetro es de: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos // 60 // 60
print(f"{segundos} segundos, equivale a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número
num = int(input("Ingrese un numero: "))
print(num * 1)
print(num * 2)
print(num * 3)
print(num * 4)
print(num * 5)
print(num * 6)
print(num * 7)
print(num * 8)
print(num * 9)
print(num * 10)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
num1 = int(input("Ingrese un numero distinto a 0: "))
num2 = int(input("Ingrese otro numero distinto a 0: "))
print(num1 + num2)
print(num1 / num2)
print(num1 * num2)
print(num1 - num2)

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
# (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
masa = peso / (altura) ** 2
print(f"Su indice de masa corporal es de: {masa}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = 9 / 5 * celsius + 32
print(f"El equivalente de {celsius}C a Fahrenheit es de: {fahrenheit}F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es de: {promedio}")