pares = []
impares = []
for i in range(1, 51): # vai de 1 até 50
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f"Números pares: {pares}\nNúmeros impares: {impares}")

pares = [i for i in range(1, 51) if i % 2 == 0] # [expressão for item in sequência if condição]
impares = [i for i in range(1, 51) if i % 2 != 0] # [expressão for item in sequência if condição]
print(f"Pares:{pares}\nImpares:{impares}")