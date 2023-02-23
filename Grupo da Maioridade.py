import datetime
data = datetime.datetime.now()
ano_atual = data.year
maior = 0
menor = 0
for c in range(1, 8):
    idade = int(input(f'Dígite a idade da {c}° pessoas do grupo:'))
    conta = ano_atual-idade
    if conta < 18:
        menor += 1
    else:
        maior += 1
print(f'possui {maior} maiores de idade e {menor} menores de idade!')
