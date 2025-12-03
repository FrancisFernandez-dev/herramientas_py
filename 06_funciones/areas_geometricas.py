def area_circulo(r):
    return 3.14159 * (r ** 2)

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

print("--- Calculadora de Áreas ---")
print("1. Círculo")
print("2. Triángulo")
print("3. Rectángulo")

op = input("Selecciona una figura: ")

if op == "1":
    r = float(input("Radio: "))
    print("Área del círculo:", area_circulo(r))

elif op == "2":
    b = float(input("Base: "))
    h = float(input("Altura: "))
    print("Área del triángulo:", area_triangulo(b, h))

elif op == "3":
    b = float(input("Base: "))
    h = float(input("Altura: "))
    print("Área del rectángulo:", area_rectangulo(b, h))

else:
    print("Opción no válida.")
