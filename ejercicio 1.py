inventario = {}
def actualizar_stock(codigo):
    if codigo in inventario:
        nueva_cantidad = int(input(f"Ingrese la nueva cantidad para el producto {codigo}: "))
        inventario[codigo]["cantidad"] = nueva_cantidad
        print("El nuevo stock es {inventario[codigo]['cantidad']}")
        return
    else:
        print("Producto no encontrado en el inventario.")

def agregar_producto():
    print("\n Agregar Producto ")
    codigo = input("Ingrese el código del producto: ")
    if codigo in inventario:
        print("\n ¿Desea actualizar el stock? ")
        print("1. Si")
        print("2. No")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("llego aca")
            actualizar_stock(codigo)
        else:
            return
    else: 
        nombre = input("Ingrese el nombre del producto: ") 
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario[codigo] = producto
        print("Producto agregado con éxito.")

def ver_inventario():
    print("\n--- Inventario ---")
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def buscar_producto():
    print("\n--- Buscar Producto ---")
    busqueda = input("Ingrese el código o nombre del producto: ").lower()
    encontrado = False
    for codigo, producto in inventario.items():
        # Buscando si la busqueda coincide con el código o el nombre (en minúsculas)
        if busqueda in codigo.lower() or busqueda in producto["nombre"].lower():
            print(f"Código: {codigo}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.")

def reporte():
    print("\n Reporte ")
    for codigo, producto in inventario.items():
        cantidad = int(producto["cantidad"])
        if cantidad < 3:
            print(f"El producto {producto['nombre']} con codigo {codigo} se encuentra con un stock critico de {cantidad}")
        elif 3 <= cantidad < 5:
            print(f"El producto {producto['nombre']} se encuentra con un stock bajo de {cantidad}")


    return
        

# --- Ejecución Principal ---
def main():
    opcion=0;
    while opcion != 5:
        print("\n Menú Principal ")
        print("1. Agregar Producto")
        print("3. Buscar Producto")
        print("4. Reporte de stock")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            reporte()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
