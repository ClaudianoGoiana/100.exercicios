salario = float(input('Digite seu salario: R$'))
if  salario <= 1250:
    print(f'Voce recebeu um aumento de 15% e seu novo salario é R${salario*1.15:.2f}') # calcula o novo salario, para salarios menores ou iguais a R$1250,00 o aumento é de 15%
else:
    print(f'voce teve um aumento de 10% e seu salario é de R${salario*1.10:.2f}') # calcula o novo salario, para salarios maiores que R$1250,00 o aumento é de 10%