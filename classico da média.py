n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual sua segunda nota: '))
n3 = float(input('Qual sua terceira nota: '))
n4 = float(input('Qual sua quarta nota: '))
m = (n1+n2+n3+n4) / 4
if m <= 5:
    print(f'Você REPROVOU! sua nota foi {m}!')
elif 5.1 <= m < 6.9:
    print(f'Você está de RECUPERAÇÃO! sua nota foi {m}!')
elif m >= 7.0:
    print(f'Você PASSOU de ano! sua nota foi {m}!')
