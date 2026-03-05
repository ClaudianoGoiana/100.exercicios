nome = str(input('Digite seu nome completo: ')).strip().upper() #.strip() remove os espaços antes e depois da frase, .upper() deixa tudo em maiúsculo
print(f'Prazer em te conhecer! ')
print(f'Seu primeiro nome é {nome.split()[0]}') #split() divide a frase em partes, [0] mostra a primeira parte da frase
print(f'Seu último nome é {nome.split()[-1]}') #[-1] mostra a última parte da frase, pois o python começa a contar do 0, então -1 é a última posição da frase