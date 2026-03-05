lista = [-8, 6, -1, 3, 4]

dev2 = []
dev3 = []
for num in lista:
    if num % 2 == 0:
        dev2.append(num)
    if num % 3 == 0:
        dev3.append(num)

print("Divisivel por dois ",len(dev2))
print("Divisivel por três ", len(dev3))


frase = "No inicil tudo é dificil." # ou poderia coloca o frase = input("Digite uma frase: ")
carac = len(frase) # aqui a variavel carac recebe a contagem dos caracteres pelo len(frase)
frase_cortada = frase.split() # Aqui a a variavel frase_cortada recebe de frase a str dividida pela frase.split() 
frase_total = len(frase_cortada) # Aqui a variavel frase__total recebe a quantidade de palavras pelo len()
print(carac)
print(frase_total)

palavra = "No inicio tudo é dificil."       # ou input("Digite um palavra: ")

vogal = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'

pv = ""

for letra in palavra:
    if letra in vogal:
        pv = letra
        break

if pv != "":
    print(pv)

else:
    print("-")
    

# raiz de delta

import math

a = 3
b = -7
c = 2

delta = b**2 - 4*a*c
print(delta)


if delta < 0:
    print(" sem raiz")
elif delta == 0:
    raiz = delta -b / (2*a)

    print(f"só tem uma raiz {raiz:.2f}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Raiz1 {raiz1:.2f} Raiz2 {raiz2:.2f}")



