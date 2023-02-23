frase = str(input('Dígite uma frase para saber sé é um Palidromo: ')).strip().upper()
pala = frase.strip()
junto= ''.join(pala)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'Temos um palidromo {inverso} e {junto}')
else:
    print('Não têmos um palidromo')
