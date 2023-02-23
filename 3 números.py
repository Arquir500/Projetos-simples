n1 = int(input('Dígite um número: '))
n2 = int(input('Dígite outro número: '))
n3 = int(input('Dígite o último número: '))
if n1 > n2 and n3:
    print(f'O número {n1} e o maior')
elif n2 > n1 and n3:
    print(f'O número {n2} e o maior')
elif n3 > n1 and n2:
    print(f'O número {n3} e o maior')
elif n1== n2 == n3:
    print('Os números são todos iguais.')