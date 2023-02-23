#nome = str(input('Qual o seu nome?')).upper()
#if nome == 'RENAN':
    #print('Que nome lindoooo')
#else:
    #print('NOME FEIO')
#print(f'Bom dia, {nome}')
n1 = float(input('Dígite sua note:'))
n2 = float(input('Dígite sua segunda nota:'))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m >=6:
    print('Você passou de ano!')
else:
    print('Você reprovou!')
print('Continué se esforçando! o futuro e feito com estudo!')