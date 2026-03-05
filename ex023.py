num = int(input("Digite um número de 0 a 9999: ")) # pede um numero de 0 a 9999
u = num // 1 % 10 # pega o numero da unidade
d = num // 10 % 10 # pega o numero da dezena
c = num //100 % 10 # pega o numero da centena
m = num // 1000 % 10 # pega o numero do milhar
print(f'Numero digitado: {num}\nUnidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}') # mostra o numero digitado e a unidade, dezena, centena e milhar