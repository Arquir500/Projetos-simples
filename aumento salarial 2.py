salario = float(input('Dígite seu sálario para saber seu aumento: '))
if salario >= 1250:
    print(f'O valor do seu sálario vai ser R${salario*0.1+salario:.2f}')
else:
    print(f'O valor do seu sálario vai ser R${salario*0.15+salario:.2f}')