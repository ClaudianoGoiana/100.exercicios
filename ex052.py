num = int(input("Digite o número inteiro: ")) # o usuario digita um numero inteiro e ele é convertido para inteiro
divisor = 0 # variavel para contar o numero de divisores do numero digitado
for i in range(1, num + 1): # o range é de 1 a num, pois o num + 1 não é incluido
    if num % i == 0: # verifica se o numero é divisivel por i, ou seja, se o resto da divisão é igual a 0
        divisor += 1 # se o numero for divisivel por i, o contador de divisores é incrementado
if divisor == 2: # se o numero tiver apenas 2 divisores, ou seja, 1 e ele mesmo, ele é primo
    print(f"O número {num} é primo.")
else: # se o numero tiver mais de 2 divisores, ele não é primo
    print(f"O número {num} não é primo.")