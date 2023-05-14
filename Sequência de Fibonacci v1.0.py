print("Sequência de Fibonacci")
print("=-"*20)
primeiroNumero = int(input("Qual termo você quer mostrar? "))
primeiroTermo = 0
segundoTermo = 1
print(f"{primeiroTermo} → {segundoTermo}", end="")
contador = 3
while contador <= primeiroNumero:
    terceiroTermo = primeiroTermo + segundoTermo
    print(f'→ {terceiroTermo} ', end="")
    primeiroTermo = segundoTermo
    segundoTermo = terceiroTermo
    contador += 1
print("→ Fim")