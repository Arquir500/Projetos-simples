import random
print('\33[33m~~\33[m'*50)
start = str(input('\33[32mVamos jogar um jogo?\33[m')).upper().strip()
Playerlife=20
monstrolife=20

print(f'\33[33mSua vida e {Playerlife}\33[m')
print(f'\33[33mA vida do monstro é {monstrolife}\33[m')


while Playerlife > 0 and monstrolife>0:
    (input('\33[31mVocê está em frente a um monstro, com sua espada empunhada está na'
           ' hora de atacar, dígite Ataque para atacar:\33[m'))
    danom = random.randrange(2,8)
    danop = random.randrange(2,12)
    monstrolife = monstrolife - danop
    Playerlife = Playerlife - danom
    if danom >=6:
        print(f'\33[33mO monstro desferiu um golpe devastador causando {danom} de dano, você têm sorte de estar vivo\33[m.')
    else:
        print(f'\33[33mO monstro te ataca ferrozmente causando {danom} de dano\33[m')
    if danop >=8:
        print(f'\33[33mVocê brandi sua espada com perfeição causando {danop} de dano\33[m')
    else:
        print(f'\33[33mVocê faz uma graça e acaba causando {danop}\33[m')
    print('\33[33m~~\33[m' * 50)
    print(f'\33[33mSeu Hp:{Playerlife} \33[m')
    print(f'\33[33mHp do monstro:{monstrolife}\33[m')
    print('\33[33m~~\33[m' * 50)
    if Playerlife <=0:
        print('Você morreu, seus anos estudos foram pro Lixo.')
    elif monstrolife <=0:
        print('Voce conseguiu derrotar o monstro!')


