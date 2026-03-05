# tempo = int(input('Quantos anos do seu carro: '))
# if tempo<=3:#se o tempo for menor ou igual a 3 anos, o carro é novo
#     print('Carro novo')

# elif tempo>3 and tempo<=5:#se o tempo for maior que 3 anos e menor ou igual a 5 anos, o carro é semi-novo
#     print('Carro semi-novo')

# else:#se o tempo for maior que 5 anos, o carro é velho
#     print('carro velho')

# print('==FIM==')

# nome = str(input('Digite seu nome: ')).strip() #.strip() remove os espaços antes e depois da frase
# if nome == 'Claudiano': #se o nome for igual a 'Claudiano', o programa vai imprimir 'Que nome lindo você tem!'
#     print('Que nome lindo você tem!')
# else: #se o nome for diferente de 'Claudiano', o programa vai imprimir 'Seu nome é bacana!'
#     print('Seu nome é bacana!')

# print(f'Bom dia {nome}!') #f'Bom dia {nome}!' é uma forma de imprimir a variável nome dentro da string, usando a letra f antes da string e colocando a variável entre chaves {}.

n1 = float(input('Digite sua primenra nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2 #média das notas
if m>=6.0: #se a média for maior ou igual a 6.0, o aluno está aprovado
    print(f'Parabéns! Você foi aprovado com média {m:.1f}!')
elif m>=4.0 and m<6.0: #se a média for maior ou igual a 4.0 e menor que 6.0, o aluno está de recuperação
    print(f'Você está de recuperação! Sua média é {m:.1f}!')
else: #se a média for menor que 4.0, o aluno está reprovado
    print(f'Infelizmente você foi reprovado te esperando no proximo ano {m:.1f}!')