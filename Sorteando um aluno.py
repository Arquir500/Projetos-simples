import random
p = str(input(' Dígite o nome do primeiro aluno: '))
s = str(input('Dígite o nome do segundo aluno: '))
t = str(input('Dígite o nome do terceiro aluno: '))
q = str(input('Dígite o nome do quarto aluno: '))
qi = str(input('Dígite o nome do quinto aluno:'))
lista = [p, s, t, q, qi]
random.shuffle(lista)
print(f'A ordem de apresentação ficou')
print(lista)

