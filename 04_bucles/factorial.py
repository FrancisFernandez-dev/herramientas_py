n = int(input("Ingresa un número para calcular su factorial: "))

factorial = 1
contador = n

while contador > 0:
    factorial *= contador
    contador -= 1

print(f"El factorial de {n} es {factorial}")
