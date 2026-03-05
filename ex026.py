frase = str(input('Digite uma frase: ')) .strip().upper()#.strip() remove os espaços antes e depois da frase, .upper() deixa tudo em maiúsculo
print(f'a letra  "A" aparece {frase.count("A")} vezes') #count() conta quantas vezes a letra aparece na frase
print(f'A letra "A" aparece pela primeira vez na posição {frase.find("A")+1}') #find() mostra a posição da letra, +1 para mostrar a posição correta, pois o python começa a contar do 0
print(f'A letra "A" aparece pela ultima vez na posição {frase.rfind("A")+1}') #rfind() mostra a posição da última letra, +1 para mostrar a posição correta, pois o python começa a contar do 0
