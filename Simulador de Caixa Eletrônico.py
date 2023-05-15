print("="*20)
print(f"Banco TXT")
valor = int(input('Que valor quer sacar? R$'))
total = valor
cedula = 50
totalCedulas = 0
while True:
    if total >=cedula:
        total -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f"Total de {totalCedulas} cédulas de R$ {cedula:.2f}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula ==10:
            cedula =1
        totalCedulas = 0
        if total == 0:
            break
print("Volte sempre!")
print("Tenha um ótimo dia!")