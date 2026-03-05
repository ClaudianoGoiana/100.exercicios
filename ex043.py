peso = float(input('Digite seu peso? (kg) '))
altura = float(input('Digite sua altura? (cm) '))
if altura > 3 : # Se a altura for maior que 3, assumimos que está em centímetros
    altura = altura / 100
imc = peso/(altura**2)

if imc < 18.5: # Se o imc for menos que 18.5 
    print(f'Abaixo do peso: {imc:.1f}')
elif imc > 18.5 and imc < 25: # Se o imc for maior que 18.5 e menor que 25
    print(f'Peso ideal: {imc:.1f}')
elif imc > 25 and imc < 30:
    print(f'Sobre peso: {imc:.1f}')
elif imc > 30 and imc < 40:
    print(f'Obesidade {imc:.1f}')
else: # Se o imc estiver acima de 40
    print(f'Obesidade mórbida: {imc:.1f}')