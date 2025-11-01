# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad

archivos_productos = open("productos.txt", "w")
archivos_productos.write("Lapicera,250,25\n")
archivos_productos.write("Goma de borrar,200,23\n")
archivos_productos.write("Regla,300,30\n")
archivos_productos.close()


# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
# formato: 
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30


lista_productos = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        nombre, precio, cantidad = linea_limpia.split(",")

        # 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
        # una lista llamada productos, donde cada elemento sea un diccionario con claves: 
        # nombre, precio, cantidad

        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        lista_productos.append(producto)

for p in lista_productos:
    print(f"Producto: {p["nombre"]} | Precio: ${p["precio"]} | Cantidad: {p["cantidad"]}")


# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
# cantidad) y lo agregue al archivo sin borrar el contenido existente

nombre_nuevo = input("Ingrese nombre del producto: ")
precio_nuevo = input("Ingrese precio del producto: ")
cantidad_nuevo = input("Ingrese cantidad del producto: ")

producto_nuevo = {
    "nombre": nombre_nuevo,
    "precio": float(precio_nuevo),
    "cantidad": int(cantidad_nuevo)
}

lista_productos.append(producto_nuevo)
print(f"Producto {nombre_nuevo} agregado a la lista")


# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
# no existe, mostrar un mensaje de error

nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ").strip()

producto_encontrado = None

for p in lista_productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        producto_encontrado = p
        break
if producto_encontrado:
    print(f"Nombre: {producto_encontrado["nombre"]}")
    print(f"Precio: {producto_encontrado["precio"]}")
    print(f"Cantidad: {producto_encontrado["cantidad"]}")
else:
    print(f"El producto {nombre_buscar} no se encuentra en la lista")

with open("productos.txt", "w") as archivo:
    for producto in lista_productos:
        linea = f"{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n"
        archivo.write(linea)
print("Datos guardados correctamente")
