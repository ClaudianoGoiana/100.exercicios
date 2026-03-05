from datetime import date
atual = date.today().year
nascimento = int(input('Data de nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print(f'Categoria MIRIM: com {idade} anos')
elif idade > 9 and idade <= 14:
    print(f'Categoria INFATIL com {idade}')
elif idade > 14 and idade <= 19:
    print(f'Categoria JUNIOR com {idade}')
elif idade > 19 and idade <= 25:
    print(f'Categoria SÊNIOR com {idade} ')
else:
    print(f'Categoria MASTER com {idade}')