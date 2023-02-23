from random import randint
import time
print('\33[33m-=\33[m'*50)
numeropc = int(input('\33[36mVamos jogar? pensei em um número de 1 á 10, consegue adinhar qual é?\33[m'))
print('\33[33m-=\33[m'*50)
print('\33[35mProcessando...\33[m')
time.sleep(0.5)
ale = randint(0, 10)
numerot = 1
while numeropc != ale:
    if numeropc > ale:
        numeropc = int(input('\33[36mO número que pensei e menor...'))
        numerot += 1
    elif numeropc < ale:
        numeropc = int(input('\33[36mO número que pensei e maior...'))
        numerot += 1
print(f'\33[34mParabéns você ganhou em {numerot} tentativas, o número que pensei foi {ale}')
print('\33[36mVamos jogar mais?\33[m')
print('\33[33m-=\33[m'*50)