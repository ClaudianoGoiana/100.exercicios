valor_casa = float(input('Qual o valor da casa: R$'))
seu_salario = float(input('Qual o seu salario: R$'))
anos_pagar = float(input('Em quantos anos você desejá pagar: '))
salario = seu_salario * 1.30
gastar = salario - seu_salario
anos = anos_pagar * 12
valor_parcelas = valor_casa/anos
if valor_parcelas <= gastar:
    print('Parabêns voce pode comprar a casa')
else:
    print('Infelismente voce tem que melhorar o seu salario')
print(f'seu salario: R${seu_salario},pode usa R${gastar}')
print(f'parcelas: {anos:.0f} valoar das parcelas{valor_parcelas:.2f}')