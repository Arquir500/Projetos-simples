from time import sleep
print('\33[33m-\33[m'*45)
casa = float(input('\33[32mQual o valor da casa que deseja comprar?\33[m'))
salario = float(input('\33[32mQual o seu salário?\33[m'))
anos = float(input('\33[32mEm quantas anos deseja pagar?\33[m'))
print('\33[33mCalculando a possibilidade do empréstimo...\33[m')
sleep(2)
valor_prestacao = casa/(anos * 12)
salario_convertido = salario*0.3
if valor_prestacao <= salario_convertido:
    print(f'Parabéns o valor da prestação é R${valor_prestacao:.2f} em {anos*12:.0f} meses e o comprometimento não afeta você no mercado R${salario_convertido:.2f}')
else:
    print(f'Infelizmente seu crédito foi negado a prestacação R${valor_prestacao:.2f} comprometi sua situação financeira R${salario_convertido:.2f}')