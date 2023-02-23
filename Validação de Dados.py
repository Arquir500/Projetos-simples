sexo = str(input('Informe seu Sexo (F/M): ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
