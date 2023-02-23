t1 = float(input('Primeiro segmento:'))
t2 = float(input('Segundo segmento:'))
t3 = float(input('Terceiro segmento:'))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os lados podem formar um triangulo!')
    if t1 == t2 == t3:
        print('E um triângulo equilátero, todos os lados são iguais.')
    elif t1 == t2 or t1 == t3 or t2 == t3:
        print('E um triângulo Isôsceles, dois lados iguais.')
    else:
        print('E um triângulo escaleno, são lados diferentes.')
else:
    print('Os lados não podem formar um triângulo!')