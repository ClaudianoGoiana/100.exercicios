n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
total = (n1 + n2) / 2
if total >= 7:
    print(f'Aprovado com {total} potos!!!')
elif total >= 4 and total <= 6.99:
    print(f'Ficou em recuperação com {total}')
else:
    print(f'Reprovado com {total}')