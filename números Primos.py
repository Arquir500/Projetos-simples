n1 = int(input('Dígite um número para saber se ele é primo:'))
tot = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\33[32m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print(f'- {c}', end='')

print(f' O número {n1} foi divisível {tot} vezes')
if tot == 2:
    print('Por isso o número é primo')
else:
    print('Por isso o número não é primo')


