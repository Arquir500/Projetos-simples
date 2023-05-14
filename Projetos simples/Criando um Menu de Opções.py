print("Bem vindo ao menu de opções de cálculo")
primeiroNumero = int(input("Qual o primeiro valor? "))
segundoNumero = int(input("Qual o segundo valor? "))
opção = 0
while opção != 6:
    print('''    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    [5] Novos números
    [6] Sair do programa''')
    opção = int(input("Qual é a sua opção? "))
    if opção == 1:
        print(f"A soma dos valores {primeiroNumero} + {segundoNumero} é {primeiroNumero + segundoNumero}")
    elif opção == 2:
        print(f"A Subtração dos valores {primeiroNumero} - {segundoNumero} é {primeiroNumero - segundoNumero}")
    elif opção == 3:
        print(f"A multiplicação dos valores {primeiroNumero} X {segundoNumero} é {primeiroNumero * segundoNumero}")
    elif opção == 4:
        print(f"A Divisão dos valores {primeiroNumero} / {segundoNumero} é {primeiroNumero / segundoNumero}")
    elif opção ==5:
        print('Informe novos valores!')
        primeiroNumero = int(input("Primeiro valor? "))
        segundoNumero = int(input("Segundo valor? "))
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print("Fim do programa")