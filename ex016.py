# num = float(input('digite um numero tipo xx.xxx: '))
# print(f'O valor digitado foi {num} e sua parte inteira é {int(num)}')

from math import trunc

num = float(input('Digite um numero decimal: '))
print(f'O valor digitado é {num} e sua parte inteira é {trunc(num)}')
