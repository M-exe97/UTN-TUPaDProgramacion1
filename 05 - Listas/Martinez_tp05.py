# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

# notas = [8, 7, 6, 7, 9, 8, 10, 10, 5, 4]
# print(f"Notas de alumnos: {notas}")
# suma = 0
# cont = 0
# for i in notas:
#     suma += i
#     cont += 1
# print(f"El promedio es de: {suma / cont:.2f}")

# mayor_nota = 0
# menor_nota = 10

# for i in notas:
#     if i > mayor_nota:
#         mayor_nota = i
#     if i < menor_nota:
#         menor_nota = i

# print(f"Nota mas alta: {mayor_nota}\nNota mas baja: {menor_nota}")

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# productos = []

# productos.append(input("Ingrese el producto numero 1: "))

# for i in range(2, 6):
#     productos.append(input(f"Ingrese el producto numero {i}: "))

# productos_ordenados = sorted(productos)
# print(productos_ordenados)

# eliminar = input("Que producto queres eliminar: ")

# if eliminar in productos_ordenados:
#     productos_ordenados.remove(eliminar)
#     print(productos_ordenados)
# else:
#     print("El producto no esta en la lista.")

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista.

# import random

# list_rand = [random.randint(1,100) for i in range(15)]
# list_par = []
# list_impar = []

# for num in list_rand:
#     if num % 2 == 0:
#         list_par.append(num)
#     elif num % 2 != 0:
#         list_impar.append(num)

# print(f"En la lista hay un total de: {len(list_par)} numeros pares y un total de {len(list_impar)} numeros impares")

# 4) Dada una lista con valores repetidos: [1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

# lista = [1,3,5,3,7,1,9,5,3]
# lista_no_repetidos = []

# for num in lista:
#     if num not in lista_no_repetidos:
#         lista_no_repetidos.append(num)
# print(lista_no_repetidos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

# lista_estudiantes = ["Pepe", "Juan", "Carlos", "Jose", "Maria", "Ramiro", "Rocio", "Monica"]

# print(lista_estudiantes)
# agregar = input("Quiere agregar un nuevo estudiante? (S/N)")
# if agregar.lower() == "s":
#     nuevo_estudiante = input("Ingrese el nombre del estudiante a agregar: ")
#     lista_estudiantes.append(nuevo_estudiante)
# elif agregar.lower() == "n":
#     pass
# else:
#     print("Debe ingresar S/N")

# eliminar = input("Quiere eliminar un estudiante existente? (S/N)")
# if eliminar.lower() == "s":
#     eliminar_existente = input("Ingrese el nombre del estudiante a eliminar: ")
#     if eliminar_existente in lista_estudiantes:
#         lista_estudiantes.remove(eliminar_existente)
#     else:
#         print("El estudiante ingresado no esta en la lista")
# elif eliminar.lower() == "n":
#     pass
# print(lista_estudiantes)

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero).

# lista = [1,2,3,4,5,6,7]
# lista = [lista[-1]] + lista[:-1]
# print(lista)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica.

# matriz = [[10, 15], [10, 14], [15, 21], [25, 28], [15, 28], [24, 26], [26, 29]]
# cantidad_filas = len(matriz)
# cantidad_columnas = len(matriz[0])
# for i in range(cantidad_filas):
#     print(matriz[i])

# suma_min = 0
# suma_max = 0
# mayor_amplitud = 0
# dia_amplitud = 0
# contador = 1

# for fila in matriz:
#     temp_min = fila[0]
#     temp_max = fila[1]

#     suma_min += temp_min
#     suma_max += temp_max

#     amplitud = temp_max - temp_min
#     if amplitud > mayor_amplitud:
#         mayor_amplitud = amplitud
#         dia_amplitud = contador
#     contador += 1

# promedio_min = suma_min / cantidad_filas
# promedio_max = suma_max / cantidad_filas

# print(f"Promedio de las minimas: {promedio_min:.2f}")
# print(f"Promedio de las maximas: {promedio_max:.2f}")
# print(f"Mayor amplitud termica: {mayor_amplitud:.2f} en el dia: {dia_amplitud}")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia.

# notas = [[8,6,8],[8,3,5],[7,9,10],[8,8,9],[9,5,7]]
# print("-----Promedio Estudiantes-----")
# cont_estudiante = 1
# for estudiante in notas:
#     promedio = sum(estudiante) / len(estudiante)
#     print(f"El promedio del estudiante {cont_estudiante} es: {promedio:.2f}")
#     cont_estudiante += 1

# cant_materias = len(notas[0])
# cant_estudiantes = len(notas)

# print("-----Promedio Materias-----")
# for j in range(cant_materias):
#     suma = 0
#     for i in range(cant_estudiantes):
#         suma += notas[i][j]
#     prom_materia = suma / cant_estudiantes
#     print(f"Promedio de la materia {j+1}: {prom_materia:.2f}")


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada.

# tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
# jugador = "X"
# turno = 0

# while turno < 9:
#         for fila in tablero:
#             for casilla in fila:
#                 print(casilla, end=" ")
#             print()

#         print(f"Turno del jugador: {jugador}")
#         fila = int(input("Ingrese la fila (1-3): ")) -1
#         columna = int(input("Ingrese la columna (1-3): ")) -1

#         if tablero[fila][columna] == "-":
#             tablero[fila][columna] = jugador
#             turno += 1
#         else:
#             print("Casilla ocupada, eleji otra")
#             continue
        
#         if jugador == "X":
#             jugador = "O"
#         else:
#             jugador = "X"

# print("Resultado final")
# for fila in tablero:
#     for casilla in fila:
#         print(casilla, end=" ")
#     print()

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana.

# ventas = [[5,6,3,7,4,6,6],[8,6,8,5,7,4,12],[9,23,12,13,15,20,18],[9,5,7,2,7,10,11]]

# print("-----Total vendido por cada Producto-----")
# cont_producto = 1
# for producto in ventas:
#     total = sum(producto)
#     print(f"Total vendido del producto {cont_producto}: {total}")
#     cont_producto += 1

# print("\n-----Dia con mayor ventas-----")
# cant_dias = len(ventas[0])
# cant_productos = len(ventas)

# mayor_venta = 0
# dia_mayor = 0

# for j in range(cant_dias):
#     suma_dia = 0
#     for i in range(cant_productos):
#         suma_dia += ventas[i][j]
#     if suma_dia > mayor_venta:
#         mayor_venta = suma_dia
#         dia_mayor = j + 1
# print(f"El dia con mayor ventas totales fue el dia: {dia_mayor} con {mayor_venta} unidades vendidas")

# print("\n-----Producto mas vendido-----")
# cont_producto = 1
# mayor_total = 0
# produ_mas_vendido = 0

# for producto in ventas:
#     total = sum(producto)
#     if total > mayor_total:
#         mayor_total = total
#         produ_mas_vendido = cont_producto
#     cont_producto += 1

# print(f"El producto mas vendido de la semana fue el: {produ_mas_vendido}, con un total de {mayor_total} unidades vendidas")
