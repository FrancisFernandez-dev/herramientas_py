agenda = {}

while True:
    print("\n=== AGENDA DE CONTACTOS ===")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda[nombre] = telefono
        print("Contacto agregado.")

    elif opcion == "2":
        print("\n--- CONTACTOS ---")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

    elif opcion == "3":
        print("Hasta luego.")
        break

    else:
        print("Opción inválida.")
