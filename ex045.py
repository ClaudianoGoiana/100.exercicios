from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print(f"{" Suas opções ":=^20}\n[0] Pedra\n[1] Papel\n[2] Tesoura")
while True:
    try: # código que pode dar erro
        jogador = int(input("Sua escolha? "))
        if jogador in [0, 1, 2]: # só aceita 0, 1, 2
            break
        else:
            print(f"Entrada invalida! Digite 0, 1, 2.")
    except ValueError: # o except se der erro ele pula para continuar o código
        print("Entrada invalida! Digite apenas números 0, 1, 2.")

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-="*11)
print(f"Jogador jogou {itens[jogador]}")
print(f"Computador jogou {itens[computador]}")
print("-="*11)
if computador == jogador:
    print(f"Empate")
elif(jogador == 0 and computador == 2) or \
    (jogador == 1 and computador == 0) or \
    (jogador == 2 and computador == 1):
    print(f"Você venceu!")
else:
    print(f"Computador venceu!")

# if computador == 0: # computador jogou Pedra
#     if jogador == 0:
#         print(f"Empate")
#     elif jogador == 1:
#         print(f"Jogador vence")
#     elif jogador == 2:
#         print(f"Computador vence")
#     # else:
#     #     print("Entrada invalida!")

# elif computador == 1:# computador jogou Papel
#     if jogador == 0:
#         print(f"Computardo vence")
#     elif jogador == 1:
#         print("Empate")
#     elif jogador == 2:
#         print("Jogador vence")
#     # else:
#     #     print("Entrada invalida")

# elif computador == 2: # aqui o computador joga Tesoura
#     if jogador == 0:
#         print("Jogador vence")
#     elif jogador == 1:
#         print("Computador vence")
#     elif jogador == 2:
#         print("Empate")
#     else:
#         print("Entrada invalida")
# # else:
# #     print("")
