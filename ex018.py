from math import radians, sin, cos, tan
an = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(an))
print(f'O valor de seno {seno:.2f}')
cosse = cos(radians(an))
print(f'O valor do cosseno {cosse:.2f}')
tang = tan(radians(an))
print(f'O valor da tangente {tang:.2f}')