from datetime import date

ano = int(input('Digite um ano para ver se ele é bissexto ou não: '))
if ano == 0:
    ano = date.today().year # se o ano for 0, ele será substituído pelo ano atual
print(f'Analisando o ano {ano}...') # imprime o ano que está sendo analisado 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # verifica se o ano é bissexto, ou seja, se ele é divisível por 4 e não é divisível por 100 ou se ele é divisível por 400
    print(f'O ano {ano} é bissexto') # imprime que o ano é bissexto
else:
    print(f'O ano {ano} não é bissexto') # imprime que o ano não é bissexto