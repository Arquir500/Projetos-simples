quantidadeProdutos = total= maisMil= menor = 0
barato =' '
while True:
    produto = str(input("Qual o produto comprado? "))
    precoProduto = float(input("Valor do produto? R$ "))
    total += precoProduto
    quantidadeProdutos +=1
    if precoProduto >1000:
        maisMil +=1
    if quantidadeProdutos == 1 or precoProduto<menor:
        menor = precoProduto
        barato = produto
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resposta == "N":
        break
print('Fim do programa')
print(f"A quantidade de produtos foi {quantidadeProdutos} o valor total foi R$ {total:.2f}")
print(f"temos {maisMil} produtos custando mais de mil reais")
print(f"O produto mais barato foi {barato} custa R${menor:.2f}")