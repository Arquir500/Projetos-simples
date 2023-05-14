'''from math import factorial
n = int(input('Dígite um número para saber seu fatorial: '))
fatorial = factorial(n)
print(f'o fatorial de {n} é {fatorial}')'''
Numero = int(input('Dígite um número para saber seu fatorial: '))
contador = Numero
Fatorial = 1
print(f'Calculando o fatorial {Numero}! =')
while contador > 0:
    print(f'{contador}', end=' ')
    print('X ' if contador > 1 else ' = ', end='')
    Fatorial *= contador
    contador -=1
print(f'{Fatorial}')
