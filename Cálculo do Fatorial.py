'''from math import factorial
n = int(input('Dígite um número para saber seu fatorial: '))
fatorial = factorial(n)
print(f'o fatorial de {n} é {fatorial}')'''
n = int(input('Dígite um número para saber seu fatorial: '))
c = n
f = 1
print(f'Calculando o fatorial {n}!', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print('X ' if c > 1 else ' = ', end='')
    f *= c
    c -=1
print(f'{f}')
