from random import choice
import time
print('\33[33m-=\33[m'*50)
numero = int(input('\33[36mVamos jogar? pensei em um número de 1 á 10, consegue adinhar qual é?\33[m'))
print('\33[33m-=\33[m'*50)
print('\33[35mProcessando...\33[m')
time.sleep(2)
lista = (1,2,3,4,5,6,7,8,9,10)
ale = choice(lista)
if numero == ale:
    print(f'\33[32mVocê acertou pensei no número {ale}, parabens!\33[m')
else:
    print(f'\33[31mVocê errou pensei no número {ale} eu ganhei!\33[m')
print('\33[36mVamos jogar mais?\33[m')
print('\33[33m-=\33[m'*50)

