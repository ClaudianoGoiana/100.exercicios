from datetime import date
atual = date.today().year
for i in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc

    if idade <= 18:
        print(f"esta pessoa é menor de idade")
    else:
        print(f"esta pessoa é maior de idade")
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')