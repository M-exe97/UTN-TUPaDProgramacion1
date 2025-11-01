# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300

# print(precios_frutas)



# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, "Naranja": 1200, "Manzana": 1500, "Pera": 2300} 

# precios_frutas["Banana"] = 1330
# precios_frutas["Manzana"] = 1700
# precios_frutas["Melón"] = 2800

# print(precios_frutas)



# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios

# precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, "Naranja": 1200, "Manzana": 1700, "Pera": 2300} 

# print(list(precios_frutas.keys()))



# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe

# contactos = {}

# for i in range(1,6):
#     nombre = str(input(f"Ingresa el nombre del Contacto {i}: "))
#     numero = int(input(f"Ingresa el numero del Contacto {i}: "))
#     contactos[nombre] = numero

# pedir_nombre = str(input("Ingrese el nombre del Contacto que desea ver su numero asociado (Si existe)"))
# print(contactos[pedir_nombre])



# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# frase = str(input("Ingrese una frase: "))

# palabras_lista = frase.lower().split()
# palabras_unicas = set(palabras_lista)
# print(palabras_unicas)

# cant_palabras = {}

# for palabra in palabras_lista:
#     if palabra in cant_palabras:
#         cant_palabras[palabra] += 1
#     else:
#         cant_palabras[palabra] = 1

# print(cant_palabras)



# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno

# alumnos = {}

# for i in range(1,4):
#     nombre = str(input(f"Ingresa el nombre del alumno {i}: "))
#     nota1 = float(input(f"Ingresa la Nota 1: "))
#     nota2 = float(input(f"Ingresa la Nota 2: "))
#     nota3 = float(input(f"Ingresa la Nota 3: "))

#     alumnos[nombre] = (nota1, nota2, nota3)

# for nombre in alumnos:
#     notas = alumnos[nombre]
#     promedio = sum(notas) / 3

#     print(f"El promedio de {nombre} es de: {promedio:.2f}")



# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

# parcial_1 = {99, 104, 100, 105, 106, 97}
# parcial_2 = {89, 110, 107, 106, 104, 100}

# ambos_parciales = parcial_1 & parcial_2
# solo_uno = parcial_1 ^ parcial_2
# al_menos_uno = parcial_1 | parcial_2

# print(f"Aprobaron ambos parciales: {ambos_parciales}")
# print(f"Aprobaron solo uno de los dos: {solo_uno}")
# print(f"Aprobaron al menos un parcial: {al_menos_uno}")



# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe

# inventario = {"Cafe": 50, "Te": 75, "Azucar": 90, "Leche": 100, "Yogurt": 80}

# while True:
#     print("\n---------- Menu Inventario ----------\n")
#     print("1. Consultar Stock de un Producto")
#     print("2. Agregar o Actualizar Stock")
#     print("3. Ver Inventario")
#     print("4. Salir\n")

#     opcion = input("Seleccione una opcion (1-4): ")

#     if opcion == "1":
#         producto = input("Ingrese el nombre del Producto a consultar: ").strip().capitalize()
#         if producto in inventario:
#             print(f"El stock actual de {producto} es: {inventario[producto]} unidades.")
#         else:
#             print(f"El producto no se encuentra en el inventario.")

#     elif opcion == "2":
#         producto = input("Ingrese el nombre del Producto a Agregar/Actualizar: ").strip().capitalize()
#         unidades = int(input(f"Ingrese cuantas unidades desea agregar al stock de {producto}: "))
#         if producto in inventario:
#             inventario[producto] += unidades
#             print(f"Stock actualizado, se agregaron {unidades} unidades al producto: {producto}")
#         else:
#             inventario[producto] = unidades
#             print(f"Producto agregado, se añadio el producto {producto} con {unidades} unidades")
    
#     elif opcion == "3":
#         print("\n ---------- Inventario Actual ----------\n")
#         for producto in inventario:
#             stock = inventario[producto]
#             print(f"- {producto}: {stock} unidades")
#         print("")

#     elif opcion == "4":
#         break

#     else:
#         print("\nIngrese una opcion valida (1-4): ")



# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
# Permití consultar qué actividad hay en cierto día y hora

# agenda = {
#     ("lunes", "10:00"): "Reunion",
#     ("martes", "15:00"): "Clase de Ingles",
#     ("miercoles","09:30"): "Entrenamiento",
#     ("jueves", "18:00"): "Clase de Prog",
#     ("viernes", "09:30"): "Entrenamiento",
#     ("sabado", "10:00"): "Ir a la biblioteca",
#     ("domingo", "12:00"): "Reunion Familiar"
# }

# consulta_dia = input("Ingrese el dia a consultar (ej: lunes): ").strip().lower()
# consulta_hora = input("Ingrese la hora a consultar (ej: 10:00): ").strip()

# consulta = (consulta_dia, consulta_hora)

# if consulta in agenda:
#     actividad = agenda[consulta]
#     print(f"El dia {consulta_dia} a las {consulta_hora} hay: {actividad}")
# else:
#     print(f"No hay ninguna actividad programada para el {consulta_dia} a las {consulta_hora}")



# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores.

# original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
# invertido = {}

# for pais in original.keys():
#     capital = original[pais]
#     invertido[capital] = pais

# print(invertido)