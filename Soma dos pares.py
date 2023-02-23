s = 0
conta = 0
for c in range(1,7):
    n1 = int(input(f'Dígite o {c}° número: '))
    if n1%2 == 0:
        s += n1
        conta +=1
print(f'A soma dos {conta} valores pares é {s}')
