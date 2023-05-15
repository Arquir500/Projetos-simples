from random import randint
print("Vamos jogar par ou ímpar!!")
print("=-"*20)
contador = 0
while True:
    computador = randint(0, 11)
    numero = int(input("Dígite um valor? "))
    escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    total = computador + numero
    if escolha in "Pp":
        if total %2 ==0:
            print(f"Parabéns você ganhou! eu joguei {computador} e você {numero} a soma é {total}")
            contador +=1
        else:
            break
    elif escolha in "Ii":
        if total %2 !=0:
            print(f"Parabéns você ganhou! eu joguei {computador} e você {numero} a soma é {total}")
            contador += 1
        else:
            break
print(f"Você perdeu! Ganhou {contador} vezes eu joguei {computador} e você {numero} a soma foi {total}!")
