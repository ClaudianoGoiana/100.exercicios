frase = 'Curso em Video Python'
print(f'{frase[5:17]}') # fatiamento da string do caractere 5 ao 16
print(f'{frase[:5]}') # do inicio ate o caractere 4, pois o 5 nao entra mais vai mostra 5 caracteres
print(f'{frase[15:]}') # do caractere 15 ate o final

frase.replace('Python','Android') # nao altera a variavel
print(frase)

frase = frase.replace('Python', 'Android') # altera a variavel pois pedi para guardar o novo valor
print(frase) # mostra a variavel alterada
frase.upper() # deixa toda a string em maiusculo
print(frase)
frase = frase.upper() # guarda a string em maiusculo na variavel
print(frase)
frase.lower() # deixa toda a string em minusculo
print(frase)
frase = frase.lower() # guarda a string em minusculo na variavel   
print(frase)
frase.capitalize() # deixa apenas o primeiro caractere em maiusculo
print(frase)
frase = frase.capitalize() # guarda a string com apenas o primeiro caractere em maiusculo na variavel
print(frase)
frase.title() # deixa o primeiro caractere de cada palavra em maiusculo
print(frase)   
frase = frase.title() # guarda a string com o primeiro caractere de cada palavra em maiusculo na variavel
print(frase)
frase.strip() # remove os espaços inuteis no inicio e no final da string
print(frase)
frase = frase.strip() # guarda a string sem os espaços inuteis no inicio e no final na variavel
print(frase)
frase.rstrip() # remove os espaços inuteis no final da string   
print(frase)
frase = frase.rstrip() # guarda a string sem os espaços inuteis no final na variavel
print(frase)
frase.lstrip() # remove os espaços inuteis no inicio da string
print(frase)        
frase = frase.lstrip() # guarda a string sem os espaços inuteis no inicio na variavel
print(frase)
frase.split() # divide a string em uma lista
print(frase)
frase = frase.split() # guarda a lista na variavel
print(frase)
frase = ' '.join(frase) # junta a lista em uma string
print(frase)
print('''Questões para pensar
         e responder antes de 
        iniciar um problema 
        de programação''') # string multilinha só com três aspas
print('Curso'in frase) # verifica se a palavra Curso esta na string frase
print(frase.find('Curso')) # mostra a posição inicial da palavra Curso na string frase
print(frase.find('video')) # mostra -1 pois a palavra video com o (v) minusculo não esta na string frase
print(frase.count('o')) # conta quantas vezes a letra o aparece na string frase
""" Dev Aprender"""
'''Tente explicar este problema para você mesmo em voz alta e peça mais   ''' 
#investigações até você compreender completamente o problema.)

lista = [10, 20, 30, 40, 50]
print(lista[1:4]) # fatiamento da lista do indice do segundo elemento ao quarto elemento
print(lista[:3]) # do inicio ate o indice 2, pois o 3 nao entra mais vai mostra 3 elementos
print(lista[2:]) # mostra apois o indice 2 ate o final