salario = float(input('Qual o seu salário? R$'))
meses = int(input('Quantos meses trabalhou?'))
novo = salario/meses
print(f'Seu salário e de R${salario:.2f} foram {meses} meses trabalhados, o valor á receber no 13° e de R${novo:.2f}')
