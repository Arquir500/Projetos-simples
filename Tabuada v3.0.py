print("=-"*10)
while True:
    numero = int(input("Qual número deseja ver a tabuada?(Número negativo encerra) "))
    print("-" * 20)
    if numero <= 0:
        break
    for contador in range(1,11):
        print(f'{numero} X {contador} = {numero * contador}')
        contador -= 1
    print("-" * 20)
print("Programa tabuada finalizado! Volte sempre")