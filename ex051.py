a1 = int(input("Digite o primeiro termo da PA: ")) # o usuario digita o primeiro termo da PA e ele é convertido para inteiro
r = int(input("Digite a razão da PA: ")) # o usuario digita a razão da PA e ela é convertida para inteiro
for i in range(10): # o range é de 0 a 9, pois o 10 não é incluido, ou seja, serão exibidos os 10 primeiros termos da PA
    print(a1 + i*r) # o primeiro termo da PA é somado com o produto do indice i e a razão r, ou seja, a1 + 0*r, a1 + 1*r, a1 + 2*r, ... a1 + 9*r