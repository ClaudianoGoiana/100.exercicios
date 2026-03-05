# 001 Encontra a primeira vogal

vogal = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
palavra = input("Digite uma palavra: ")
p_v = "-"

for letra in palavra:
    if letra in vogal:
        p_v = letra
        break # para o loop na primeira vogal encontrada
print(p_v)

# 002 Programa para contar caracteres e palavras

# frase = input("Digite uma frase: ")
# carac = len(frase)
# palavras = frase.split()
# t_palavras = len(palavras)
# 
# print(f"Total de caracteres: {carac}")
# print(f"Palavras: {t_palavras}")


# 003 Mostra qual o time é campeão ou o empate

# c = input("Gools do Campinese: ")
# t = input("Gools do Treze: ")
# if c > t:
#     print("Campinense")
# elif c < t:
#     print("Treze")
# else:
#     print("Empate")


# 004 Media do aluno

# n1 = float(input())
# n2 = float(input())
# n3 = float(input())
# 
# p1 = 2.0
# p2 = 3.0
# p3 = 5.0
# 
# peso = p1 + p2 + p3
# 
# n_p = (n1*p1 + n2*p2 + n3*p3) / peso
# 
# print(n_p)

# 005 Baskara delta
# import math
# 
# a = int(input())
# b = int(input())
# c = int(input())
# 
# delta = b**2 - 4*a*c
# 
# if delta < 0:
#     print("Sem raiz")
# elif delta == 0:
#     raiz = -b / 2*a
#     print(f"Raiz unica: {raiz}")
# else:
#     x1 = (-b + math.sqrt(delta)) / (2*a)
#     x2 = (-b - math.sqrt(delta)) / (2*a)
#     print((f"Raiz1: {x1:.2f} Raiz2: {x2:.2f}"))

# 006 A <= B mostre as somas dos inteiros positivo e negativo entre A e B, como tambem
# se o resultado da soma total é positivo, neutro ou negativo, não pode usar (sum())

# a = int(input())
# b = int(input()) 
# 
# s_positiva = 0
# s_negativa = 0
# 
# for num in range(a, b +1):
#     if num > 0:
#         s_positiva = s_positiva + num
#     elif num < 0:
#         s_negativa = s_negativa + num
# 
# s_t = s_positiva + s_negativa
# 
# print(f"Soma positiva: {s_positiva}\nSoma negativa: {s_negativa}\nSoma total: {s_t} ") 
# 
# if s_t == 0:
#     print("Soma neutra")
# elif s_t > 0:
#     print("Positivo")
# else:
#     print("Negativo")

# 007 Avaliar o valor e mostra seu antecessor e sucessor
# 
# v = int(input())
# a = v - 1
# s = v + 1
# 
# print(f"Valor: {v}\nAntecessor: {v-1}\nSucessor {v+1}")

# 008 Dobro, Triplo, Raiz Quadrada
# from math import sqrt
# # 
# # 
# n = int(input("Digite um número: "))
# d = n*2
# t = n*3
# #r = sqrt(n) #
# r = n**(1/2)
# print(f"O dobro de {n} vale {d}.\nO tripo de {n} vale {t}.\nA raiz quadrada de {n} é igual a {r:.2f}")


# Nota do aluno digite as duas notas simples

# n1 = float(input("Primeira nota: "))
# n2 = float(input("Segunda nota: "))
# s = (n1 + n2) / 2
# print(f"Sua media foi de: {s:.2f}")

# Conversor de medidas
# m = float(input("Uma distancia em metros: "))
# cm = m * 100
# mm = m * 1000
# 
# print(f"""O seu valor comrresponde a:
# {cm:.0f} Centimetros
# {mm:.0f} Milimetros """)