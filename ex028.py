import random
n = int(input('Digite um numero: de 1 a 5: '))
r = random.randint(1,5) #gera um número aleatório entre 1 e 5
if random.randint(1,5) == n:
    print('Parabêns! você acertou!')
else:
    print(f'o nomero sorteado foi {r} e você digitou {n}. Tente novamente!')    