print(f'{'LOJAS RESETPRINT':=^40}')
preco = float(input('Preço das compras: '))
desconto = preco * 0.10
desconto_5 = preco * 0.05
desconto_20 = preco * 0.20
valor20 = preco + desconto_20
valor_desc5 = preco - desconto_5
valor_des = preco - desconto
print(f'FORMAS DE PAGAMENTO')
print(f'[1] á vista dinheiro/PIX\n[2] á vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
forma = int(input(f'Qual é a opção? '))
if forma == 1:
    print(f'Sua compra de {preco:.2f} vai ficar por {valor_des:.2f}')
elif forma == 2:
    print(f'Sua compra de {preco:.2f} vai ficar por {valor_desc5:.2f}')
elif forma == 3:
    print(f'Seu pagamento vai ficar em duas parcelas de {preco /2:.2f} no total de {preco:.2f}')

elif forma == 4:
#    preco = float(input("Digite o valor da compra: R$ "))

    # Loop para garantir que o usuário digite um número válido
    while True:
        totparc = int(input("Quantas parcelas (3 a 10)? "))
        if 3 <= totparc <= 10:   # condição correta
            break
        else:
            print("Número de parcelas inválido. Digite novamente entre 3 e 10.")

    # cálculo da taxa de juros progressiva
    passo = (20 - 5) / (10 - 3)   # ≈ 2.14% por parcela extra
    juros = 5 + (totparc - 3) * passo

    total = preco * (1 + juros/100)
    parcela = total / totparc

    print(f"Sua compra será parcelada em {totparc}x de R${parcela:.2f}")
    print(f"Taxa de juros aplicada: {juros:.1f}%")
    print(f"Total com juros: R${total:.2f}\n")
    print(f'{'PARCELAS':=^20}')
    for i in range(1, totparc + 1):
                print(f"Parcela {i}: R${parcela:.2f}")
print(f'{'PARCELAS':=^20}')

# elif forma == 4:
#     # total =preco + (preco*20/100)
#     # totparc = int(input('Quantas parcelas (3 a 10)?  '))
#     # parcela = total / totparc
#     # print(f'Sua compra serar parcelada em {totparc:.0f}X de R${parcela:.2f} no total de {total:.2f}')
# # Primeiro pedimos o valor da compra
# #preco = float(input("Digite o valor da compra: R$ "))

# # Depois perguntamos quantas parcelas o cliente deseja
#     while True:
#         totparc = int(input("Quantas parcelas (3 a 10)? "))
        
#     # Verificamos se o número de parcelas está dentro do intervalo permitido
#         if 3 <=  or totparc <= 10:
#             break 
            
#         else:
#             print("Número de parcelas inválido. Escolha entre 3 e 10.")
#     # Aqui calculamos o "passo" do aumento dos juros.
#     # Juros começam em 5% (quando são 3 parcelas) e vão até 20% (quando são 10 parcelas).
#     # A diferença é 15% (20 - 5), dividida por 7 intervalos (10 - 3).
#     passo = (20 - 5) / (10 - 3)   # ≈ 2.14% por parcela extra

#     # Fórmula para calcular o juros aplicado conforme o número de parcelas escolhido
#     juros = 5 + (totparc - 3) * passo

#     # Calculamos o valor total da compra já com os juros aplicados
#     total = preco * (1 + juros/100)

#     # Calculamos o valor de cada parcela dividindo o total pelo número de parcelas
#     parcela = total / totparc

#     # Exibimos as informações principais para o cliente
#     print(f"Sua compra será parcelada em {totparc}x de R${parcela:.2f}")
#     print(f"Taxa de juros aplicada: {juros:.1f}%")
#     print(f"Total com juros: R${total:.2f}\n")

#     # Este laço for mostra cada parcela numerada (1 até o total de parcelas)
#     for i in range(1, totparc + 1):
#         print(f"Parcela {i}: R${parcela:.2f}")