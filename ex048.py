total = 0

for i in range(1, 501):   # percorre de 1 até 500
    if i % 2 != 0 and i % 3 == 0:   # condição: ímpar e múltiplo de 3
        total += i

print(f"Soma total: {total}")