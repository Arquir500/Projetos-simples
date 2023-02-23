import math
angulo = float(input(' Dígite um ângulo: '))
r = math.radians(angulo)
cs = math.cos(r)
s  = math.sin(r)
t  = math.tan(r)
print(f'O ângulo {angulo} têm o cosseno de {cs:.2f}')
print(f'O ângulo {angulo} têm o seno de {s:.2f}')
print(f'O ângulo {angulo} têm a tangente de {t:.2f}')
