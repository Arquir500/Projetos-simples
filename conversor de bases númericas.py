n = int(input('Dígite um número inteiro para conversão:'))
print('''Escolha uma das bases para conversão:
 [1] converter em binário
 [2] converter em Octal
 [3] converter em Hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
    print(f'{n} em binário é igual á {bin(n)[2:]}')
elif op == 2:
    print(f' {n} em Octal é igual á {oct(n)[2:]}')
elif op == 3:
    print(f'{n} em Hexadecimal é igual á {hex(n)[2:]}')
else:
    print('A opção selecionada não existe!')