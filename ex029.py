vel = float(input('Digite a velocidade que estava dirigindo: '))
multa = (vel-80)*7 # calculo da multa, cada km acima de 80km/h custa R$7,00
if vel > 80: # verifica se a velocidade é maior ou igual a 80km/h
    print(f'Voce foi multado em R${multa:.2f} por esta a {vel}km/h em uma via de 80km/h') # imprime o valor da multa
else:
    print(f'Voce esta de parabêns')