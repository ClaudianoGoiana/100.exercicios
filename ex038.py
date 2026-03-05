# Escreva um programa que leia dois numeros e compare-os, mostrando na tela
# uma mensagem:
#
#-O primeiro valor é maior
#-O segundo valor é maior
#-Não existe valor maior, os dois são iguais

a = int(input('Digite um valor: '))
b = int(input('Digite o segundo valor: '))
if a > b:
    print(f'O primeiro valor é maior {a}')
elif b > a:
    print(f'O segundo valor é maior {b}')
else:
    print(f'Não existe valor maior primeiro: {a} segundo {b}')

