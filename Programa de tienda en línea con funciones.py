# Programa de tienda en línea con funciones permitidas en el curso

# Mostrar información de productos
print("=== TIENDA EN LÍNEA - REGISTRO DE VENTAS ===")
print("")
print("Productos disponibles:")
print("1. Camiseta polo - $18.50")
print("2. Pantalón jogger - $25.00")
print("3. Camisa manga larga - $30.00")
print("4. Cinturón - $10.00")
print("5. Pantalón jean - $18.00")
print("")

# Lista de precios según el número de producto
precios = [18.50, 25.00, 30.00, 10.00, 18.00]

# Lista para guardar las ganancias por cada ítem
ganancias_por_item = []

# Variable para acumular la ganancia total
ganancia_total = 0

# Solicitar número de ventas a registrar
num_ventas = int(input("¿Cuántas ventas desea registrar? "))

# Bucle para registrar cada venta
for i in range(num_ventas):
    print("")
    print(f"--- Venta {i + 1} ---")
    
    # Solicitar número de producto
    numero_producto = int(input("Ingrese el número de producto (1-5): "))
    
    # Validar que el producto esté en el rango correcto
    if numero_producto >= 1 and numero_producto <= 5:
        # Solicitar cantidad vendida
        cantidad = int(input("Ingrese la cantidad vendida: "))
        
        # Calcular ganancia del ítem
        precio = precios[numero_producto - 1]
        ganancia_item = precio * cantidad
        
        # Agregar ganancia a la lista
        ganancias_por_item.append(ganancia_item)
        
        # Acumular en la ganancia total
        ganancia_total += ganancia_item
        
        print(f"Ganancia de este ítem: ${ganancia_item:.2f}")
    else:
        print("Producto no válido. No se registró esta venta.")
        pass

# Mostrar resultados finales
print("")
print("=" * 50)
print("RESUMEN DE VENTAS DEL DÍA")
print("=" * 50)
print(f"Ganancia diaria total: ${ganancia_total:.2f}")
print("")
print("Ganancias por cada ítem vendido:")

# Mostrar cada ganancia de la lista
for i in range(len(ganancias_por_item)):
    print(f"  Ítem {i + 1}: ${ganancias_por_item[i]:.2f}")

print("")
print(f"Lista de ganancias: {ganancias_por_item}")