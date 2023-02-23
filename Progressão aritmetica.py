print('Progressão aritmetica de 10')
n1 = int(input('Digíte o primeiro termo: '))
n2 = int(input('Dígite a razão: '))
decimo = n1 + (10 - 1) * n2
for c in range(n1, decimo+n2, n2):
    print(c, end=('- '))
print('Acabou!')