# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nome com todas as letras maiusculas
# 2 - O nome com todas as letras minusculas
# 3 - Quantas letras ao todo (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

nome = Str(input("Digite seu nome completo: ")) # pede o nome completo do usuario
sem_espaco = nome.replace(' ','') # remove os espaços da string
print(f'{nome}')
print(f'Seu nome tem ao todo {len(sem_espaco)} letras sem espaços')
print(f'{nome.upper()}') # deixa toda a strig em maiusculo
print(f'{nome.lower()}') # deixa toda a string em minusculo
separa = nome.split() # divide a string em uma lista
print(f'{separa[0]}') # mostra o segundo nome
print(f'{len(separa[0])}') # mostra quantas letras tem o primeiro nome
print(f'{nome}') # mostra o nome completo
print(f'{nome.capitalize()}')
print(f'{nome.title()}') # deixa o primeiro caractere de cada letra em maiusculo