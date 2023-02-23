import random
from time import sleep
print('\33[33m-=\33[m'*30)
lista = ['pedra', 'papel', 'tesoura']
computador = random.randint(0,2)
print('\33[31mVamos jogar pedra papel tesouta!\33[m')
print('''\33[35mFaça sua escolha
 [0] Pedra
 [1] Papel
 [2] Tesoura\33[m''')
jogador = int(input('\33[97mFaça sua jogada: \33[m'))
print('\33[36mJO\33[m')
sleep(1)
print('\33[36mKen\33[m')
sleep(1)
print('\33[36mPO\33[m')
sleep(1)
print('\33[31m-=\33[m'*35)
print('computador jogou', (lista[computador]))
print('Jogador jogou', (lista[jogador]))
print('\33[31m-=\33[m'*35)
if computador == 0: #pedra
    if jogador ==0:
        print('\33[90m-=\33[m' * 35)
        print('Empatamos')
        print('\33[90m-=\33[m' * 35)
    elif jogador == 1:
        print('\33[32m-=\33[m' * 35)
        print('Jogador vence')
        print('\33[32m-=\33[m' * 35)
    elif jogador ==2:
        print('\33[31m-=\33[m' * 35)
        print('Computador vence')
        print('\33[31m-=\33[m' * 35)
    else:
        print('Jogada inválida')
elif computador == 1: #papel
    if jogador == 0:
        print('\33[31m-=\33[m' * 35)
        print('Computador vence')
        print('\33[31m-=\33[m' * 35)
    elif jogador == 1:
        print('\33[90m-=\33[m' * 35)
        print('Empatamos')
        print('\33[90m-=\33[m' * 35)
    elif jogador == 2:
        print('\33[32m-=\33[m' * 35)
        print('Jogador vence!')
        print('\33[32m-=\33[m' * 35)
    else:
        print('Jogada inválida')
elif computador == 2: #tesoura
    if jogador == 0:
        print('\33[32m-=\33[m' * 35)
        print('Jogador vence!')
        print('\33[32m-=\33[m' * 45)
    elif jogador == 1:
        print('\33[31m-=\33[m' * 45)
        print('computador venceu!')
        print('\33[31m-=\33[m' * 45)
    elif jogador == 2:
        print('\33[90m-=\33[m' * 45)
        print('Empatamos')
        print('\33[90m-=\33[m' * 45)
    else:
        print('Jogada inválida')