import datetime
nascimento = int(input('Qual seu ano de nascimento: '))
data = datetime.datetime.now()
data_atual = data.year
idade = data_atual - nascimento
if idade <= 9:
    print(f'Pela sua idade de {idade} anos, Você e classificado como Mirim!')
elif idade <=14:
    print(f'Pela sua idade de {idade} anos, Você e classificado como infantil!')
elif idade <=19:
    print(f'Pela sua idade de {idade} anos, Você e classificado como Junior!')
elif idade <=20:
    print(f'Pela sua idade de {idade} anos, você e classificado como Sênior!')
else:
    print(f'Por ter {idade} anos, você e classificado como master!')