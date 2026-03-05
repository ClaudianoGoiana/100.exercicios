a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))
if a < b and a < c: # verifica se o numero a é menor que os outros dois numeros
    print(f'O numero {a} é o menor') # imprime que o numero a é o menor
elif b < a and b < c: # verifica se o numero b é menor que os outros dois numeros
    print(f'O numero {b} é o menor') # imprime que o numero b é o menor
elif c < a and c < b: # verifica se o numero c é menor que os outros dois numeros
    print(f'O numero {c} é o menor') # imprime que o numero c é o menor
if a > b and a > c: # verifica se o numero a é maior que os outros dois numeros
    print(f'O numero {a} é o maior') # imprime que o numero a é o maior 
elif b > a and b > c: # verifica se o numero b é maior que os outros dois numeros
    print(f'O numero {b} é o maior') # imprime que o numero b é o maior 
elif c > a and c > b: # verifica se o numero c é maior que os outros dois numeros
    print(f'O numero {c} é o maior') # imprime que o numero c é o maior
