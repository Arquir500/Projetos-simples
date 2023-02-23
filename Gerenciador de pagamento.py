valor = float(input('Qual o valor do produto? '))
pagamento = str(input('Qual o tipo de pagamento? á vista Dinheiro/Cheque? á vista no cartão? e possível 2x no cartão sem juros, ou 3x com juros: ')).upper().strip()
if 'DINHEIRO' in pagamento or 'CHEQUE' in pagamento:
    print(f'O valor em pagamento á vista em Dinheiro/Cheque fica de R${valor-(valor*0.1):.2f}')
elif 'CARTÃO' in pagamento:
    print(f'O valor em pagamento á vista no cartão é R${valor-(valor*0.05):.2f}')
elif '2X' in pagamento:
    print(f'O valor a ser pago vai ser R${valor:.2f}')
elif '3X' in pagamento:
    print(f'O valor a ser pago vai ser R${(valor*0.2)+valor}')