n1 = int(input('\33[33mDígite o primeiro valor: '))
n2 = int(input('Dígite o segundo valor: '))
escolha = 0
while escolha != 5:
    print('=-=' * 12)
    print('''\33[32mOqué deseja fazer com esses número?
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos números
          [5] Sair do programa''')
    escolha = int(input('Qual opção deseja?'))
    if escolha == 1:
        print(f'A soma dos valores {n1} + {n2} = {n1+n2}')
    elif escolha == 2:
        print(f'A multiplicação dos valores {n1} X {n2} = {n1*n2}')
    elif escolha == 3:
        if n1>n2:
            print(f'O número {n1} é maior que {n2}')
        elif n1==n2:
            print(f'Ós números são iguais')
        else:
            print(f'O número {n2} é maior que {n1}')
    elif escolha == 4:
        n1 = int(input('Dígite o primeiro valor: '))
        n2 = int(input('Dígite o segundo valor: '))
    else:
        print('Opção inválida')
print('Programa finalizado')
