dis = int(input('Digite a distancia da sua viagem em km: '))
# if dis <=200: # verifica se a distancia é menor ou igual a 200km
#     print(f'o valor da distancia fica por {dis*0.50:.2f}') # calcula o valor da pasagem, para viagens de até 200km o valor é de R$0,50 por km, para viagens acima de 200km o valor é de R$0,45 por km
# else:
#     print(f'o valor da sua pasagem fica por  {dis*0.45:.2f}') # calcula o valor da pasagem, para viagens de até 200km o valor é de R$0,50 por km, para viagens acima de 200km o valor é de R$0,45 por km
preco = dis * 0.50 if dis <= 200 else dis * 0.45
print(f'o valor da sua passagem fica por R${preco:.2f}')