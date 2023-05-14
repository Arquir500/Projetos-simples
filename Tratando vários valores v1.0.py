numeros = contador = numeroSoma=0
numeros = int(input("Dígite um valor [999 para parar]: "))
while numeros !=999:
    contador +=1
    numeroSoma += numeros
    numeros = int(input("Dígite um valor [999 para parar]: "))
print(f"Você digitou {contador} números, a soma entre eles é {numeroSoma}")
