import datetime
nascimento = int(input('Vamos verificar se seu alistamento militar qual ano do seu nascimento:'))
data = datetime.datetime.now()
ano_atual = data.year
conta = ano_atual - nascimento
print(f'Você nasceu em {nascimento}, possui {ano_atual - nascimento} anos!')
if conta < 18:
    print(f'Seu alistamento militar falta {18-conta} anos, você vai se alistar em {(18-conta) + ano_atual}!')
elif conta > 18:
    print(f'Seu alistamento militar passou {conta-18} anos!, você deveria ter se alistado em {ano_atual- (conta-18)}')
else:
    print('Esse e seu ano de alistamento!')
