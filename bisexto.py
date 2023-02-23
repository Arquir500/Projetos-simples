import calendar
ano = int(input('Vamos verificar se o ano e bisexto, dítite um ano: '))
if calendar.isleap(ano):
    print('O ano e bisexto')
else:
    print('O ano não e bisexto')
