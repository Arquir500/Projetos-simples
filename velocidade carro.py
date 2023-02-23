velocidade = int(input('Velocidade percorida:'))
if velocidade >= 80:
    valor = (velocidade - 80) * 7
    print('Você passou da velocidade máxima permitida! Será multado em R$7,00 por KM/h ultrapassado'" "
          f'fica o valor de R${valor}')
else:
    print('Está dentro da velocidade permitida!')
print('Em caso de dúvidas entre em contato com o Detran.')