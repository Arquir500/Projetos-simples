from math import hypot
x = float(input('Dígite o valor do cateto oposto: '))
y = float(input('Dígite o valor do cateto adjacente: '))
print(f'Os valores dos catetos {x} e {y} formaram o cateto é {hypot(x,y)}')