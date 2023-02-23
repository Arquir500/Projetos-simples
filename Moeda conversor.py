r = float(input('Quantas dinheiro têm na sua carteira? '))
dolar = r/5.38
euro  = r/5.56
iene  = r/0.038
kz    = r/0.011
p     = r/0.033
print(f'Com R${r:.2f} você consegue comprar')
print(f'US${dolar:.2f} Doláres')
print(f'EUR${euro:.2f} Euros')
print(f'YEN${iene:.2f} Ienes')
print(f'KZ${kz:.2f} Kwanzas')
print(f'P${p:.2f} Pesos')

