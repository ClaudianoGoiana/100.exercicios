# nome = input("nome")
# idade = int(input("idade"))
# peso = float(input("seu peso"))
# print(f"Bem vindo {nome} Sua idade é {idade} e seu peso {peso}")
import math
# Obter as três notas do usuário
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# Definir os pesos
p1 = 2.0
p2 = 3.0
p3 = 5.0

media_peso = p1 + p2 + p3
media_total = (n1*p1+n2*p2+n3*p3)/media_peso
print(f"{media_total}") 