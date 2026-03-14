# dias = int(input('Digite quantos dias esta com o carro: '))
# km = int(input('Digite quantos kilometros foi rodados'))
# valor = (dias * 60) + (km * 0.15)
# print(f'O total a pagar {valor:.2f}')

def tabuada(numero):
    print(f"Tabuada do {numero}:")
    i = 1
    while i <= 10:
        print(f"{numero} x {i:2} = {numero * i}")
        i += 1

num = int(input("digite um numero para saber a tabuada: "))
print(f'{"="*12}')
tabuada(num)
print(f'{"="*12}')
