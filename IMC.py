print('Vamos cálcular seu IMC')
Peso = float(input('Qual seu peso: '))
Altura= float(input('Qual a sua altura: '))
IMC = Peso/(Altura**2)
if IMC <= 18.5:
    print(f'Seu IMC é {IMC:.1f}, Você está abaixo do peso!')
elif 18.5 < IMC < 25:
    print(f'Seu IMC é {IMC:.1f}, Você está no peso ideal!')
elif 25 < IMC < 30:
    print(f'Seu IMC é {IMC:.1f}, você está sobrepeso')
elif 30 < IMC < 40:
    print(f'Seu IMC é {IMC:.1f}, Você está obeso')
elif IMC >= 40:
    print(f'Seu IMC é {IMC:.1f}, você está com obesidade mórbida')