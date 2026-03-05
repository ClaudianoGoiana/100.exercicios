from datetime import date
atual = date.today().year
nasc = int(input('Digite ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos de idade! ')
if idade == 18:
    print(f'Esta no tempo de alistamento!')
elif idade < 18:
    at = 18 - idade
    ano = atual + at
    print(f'Falta {at} anos para se alistar!\nVocê voce vai se alistar: {ano}')
elif idade > 18:
    dep = idade - 18
    ano = atual - dep
    print(f'Tenha cuidado pois já pasou {dep} anos para seu alistamanto!\nSeu alitamento foi nos {ano}')
else:
    print('Data incorreta')