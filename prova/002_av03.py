palavra = input()
vogal = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

primeira_vogal_encontrada = ''

for letra in palavra:
    if letra in vogal:
        primeira_vogal_encontrada = letra
        break
if primeira_vogal_encontrada != '':
        print(primeira_vogal_encontrada)
else:
        print("-")


# minha_palavra = input("Digite uma palavra: ")

# vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# primeira_vogal_encontrada = ''

# for letra_atual in minha_palavra:
#     if letra_atual in vogais:
#         primeira_vogal_encontrada = letra_atual
#         break # Para o loop assim que encontrar a primeira vogal

# # print("\n--- RESULTADO ---")
# if primeira_vogal_encontrada != '':
#     print(primeira_vogal_encontrada)
# else:
#     print("-")