resposta = "S"
soma =  quantidade = media = maior = menor = 0
while resposta in "Ss":
    numero = int(input("Dígite um número: "))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input("Quer continuar? {S/N} ")).upper().strip()[0]
media = soma / quantidade
print(f"Você digitou {quantidade} números, a média foi de {media}!")
print(f'O maior número foi {maior} e o menor foi {menor}')