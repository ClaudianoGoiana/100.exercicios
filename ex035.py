a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
print(f'{"-="*20}\n       Analisandor de triângulos\n{"-="*20}')
if a + b > c and a + c > b and b + c > a:
    print('Podem formar um triângulo')
else:
    print('Não pode formar o triângolo')