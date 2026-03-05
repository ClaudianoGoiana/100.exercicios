a = int(input('Digite uma medida: '))
b = int(input('Digite a segunda medida: '))
c = int(input('Digite a terceira medida: ')) 
if a < b + c and b < a + c and c < a + b:
    print(f'Pode forma um triangulo', end='')
    if a == b == c:
        print(' Equilátrero')
    elif a != b != c != a:
        print(' Escaleno')
    else:
        print(' Isósceles')
else:
    print('Não pode forma um triangulo com estas medidas ')