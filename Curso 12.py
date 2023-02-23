nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Renan':
    print('Seu nome e bem bonito!')
elif nome == 'Jose' or nome == 'Maria':
    print('Seu nome e bem popular!')
elif nome == 'Gabriel' or nome == 'Miguel':
    print('Seu nome e de um anjo!')
elif nome == 'Arquimedes' or nome == 'Rubert':
    print('Seu nome e lendário!')
else:
    print(f'Seu nome e normal!')
print(f'Tenha um bom dia, {nome}!')