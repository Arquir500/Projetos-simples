n1 = int(input('Dígite um número:'))
n2 = int(input('Agora dígite outro número:'))
if n1 > n2:
    print(f'O número {n1} e maior que {n2}!')
elif n2 > n1:
    print(f'O número {n2} e maior que {n1}!')
else:
    print(f'Não existe número maior, os dois são iguais.')