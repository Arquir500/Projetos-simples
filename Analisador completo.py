soma_idade = 0
media_idade = 0
maioridade_homem= 0
nome_velho = ''
totmulher = 0
for p in range(1, 5):
    print(f'-----{p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maioridade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media_idade = soma_idade / 4
print(f'A média das idades e igual á {media_idade}')
print(f'O nome do homem mais velho é o {nome_velho} e têm {maioridade_homem}')
print(f'Ao todo são {totmulher} menores de 20 anos')
