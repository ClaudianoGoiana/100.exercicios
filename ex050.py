total = 0 # variavel para armazenar a soma dos numeros pares
for i in range(1,7): # o range é de 1 a 6, pois o 7 não é incluido
    num = int(input("Digite um numero: ")) # o usuario digita um numero e ele é convertido para inteiro
    if num % 2 == 0: # verifica se o numero é par, ou seja, se o resto da divisão por 2 é igual a 0
        total += num # se o numero for par, ele é adicionado ao total
print(total)