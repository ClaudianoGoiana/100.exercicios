num = int(input('Digite um numero inteiro: '))
print('Qual o tipo de conversão:\n-1 Para binário\n-2 Para octal\n-3 Para hexadecimal')
conversao = int(input('?'))
if conversao == 1:
    binario = bin(num)[2:]
    print(f'Conversão para binário: {binario}')

elif conversao == 2:
    octal = oct(num)[2:]
    print(f'Conversão para octal: {octal}')

elif conversao == 3:
    hexa = hex(num) [2:]
    print(f'Conversão para hexadecimal: {hexa}')

else:
    print('Seu numero foi invalido! reinicia o programa!')