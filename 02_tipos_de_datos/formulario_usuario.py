print("=== FORMULARIO DEL USUARIO ===")

nombre = input("Nombre: ")                    # string
edad = int(input("Edad: "))                   # entero
altura = float(input("Altura en metros: "))   # flotante
estudia = input("¿Estudias actualmente? (si/no): ")

estudia_bool = estudia.lower() == "si"        # booleano

print("\n--- RESUMEN ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"¿Estudia?: {estudia_bool}")
