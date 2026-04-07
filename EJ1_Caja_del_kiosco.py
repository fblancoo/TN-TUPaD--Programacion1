nombre = ""
# Se pide nombre y se valida que sean solo letras y no esté vacío
while not nombre.isalpha():
    nombre = input("Ingrese el nombre del cliente: ")

cantidad = "0"
# Se valida que la cantidad sea un número y mayor a 0
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Cantidad de productos a comprar: ")
cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0

# Bucle for por cada producto
for i in range(1, cantidad + 1):
    precio = ""
    while not precio.isdigit() or int(precio) < 0:
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)

    descuento = ""
    # Validación de 'S' o 'N' (manejando mayúsculas y minúsculas)
    while descuento.lower() != "s" and descuento.lower() != "n":
        descuento = input("Descuento (S/N): ").lower()

    total_sin_descuentos += precio

    if descuento.lower() == "s":
        total_con_descuentos += precio * 0.90  # Aplica 10% descuento
    else:
        total_con_descuentos += precio

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

# Muestra de datos
print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
