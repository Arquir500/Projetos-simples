diasAlugados = int(input('Por quantos dias ficou com o carro alugado? :'))
KmRodado   = float(input('Quantos Km rodou com o carro? :'))
valor1   = diasAlugados*60
valor2   = KmRodado*0.15
valorfinal = valor1+valor2
print(f'O valor a pagar pelos dias alugados {diasAlugados} e KM percorrido {KmRodado} vai ser de R${valorfinal:.2f}')
