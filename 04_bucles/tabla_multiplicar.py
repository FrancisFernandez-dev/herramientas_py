num = int(input("Ingresa un número para su tabla: "))

print(f"\nTabla del {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")