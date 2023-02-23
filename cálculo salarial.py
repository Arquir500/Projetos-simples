salario = float(input('Qual é o salaria do funcionário? R$'))
novo = salario + (salario*15/100)
print(f'Seu salaria era R${salario:.2f} com o aumento de 15% ele ficou R${novo:.2f}')