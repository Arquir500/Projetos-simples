t1 = float(input('Primeiro segmento:'))
t2 = float(input('Segundo segmento:'))
t3 = float(input('Terceiro segmento:'))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os lados podem formar um triangulo!')
else:
    print('Os lados não podem formar um triângulo!')