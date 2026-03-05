# nome = "Gemini"
# idade = 30
# preco = 9.99
# print()

# for (Loops): Para repetir um bloco de código um número 
# específico de vezes ou para cada item em uma sequência.

# for i in range(5):
#     print(i)
# frutas = "maçã", "banana", "laranja"
# for fruta in frutas:
#     print(fruta)

# while (Loops): Para repetir um bloco de código enquanto uma condição for verdadeira.
# contador = 0
# while contador < 3:
#     print(contador)
#     contador += 1 # contador = contador + 1

# Funções: Blocos de código reutilizáveis que realizam uma tarefa específica.
# def saudacao(nome):
#     return "Ola, " + nome + "!"
# mensagem = saudacao("Maria")
# print(mensagem)
import datetime # Importa a biblioteca datetime no início do arquivo
nome = input("Digite seu nome ")
ano_nascimento = int(input("Digite o ano de nascimento "))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento
if idade <= 0:
    print(f" Olá {nome} O ano de nascimento digitado está no futuro. Por favor, digite um ano válido.")
elif idade < 18:
    print(f" Olá {nome} Voçê é menor de idade com {idade} anos.")
elif idade > 110:
    print(f"Olá {nome} Sua idade atual é de: {idade} anos Você tem mais de 110 anos! Que longevidade incrível!")
else:
    print(f"Olá {nome} sua idade {idade} anos")

