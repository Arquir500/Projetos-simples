viagem = float(input('Qual a KM da viagem?'))
valor1 = viagem*0.50
valor2= viagem*0.45
if viagem <= 200:
    print(f'O valor da sua viagem vai ser \33[1;32mR${valor1:.2f}\33[m')
else:
    print(f'O valor da sua viagem vai ser \33[1;32mR${valor2:.2f}\33[m')
print('\33[34mÒtima viagem!\33[m')