from math import hypot
ca = int(input('Qual o valor do cateto adjacente: '))
co = int(input('Qual o valor do cateto oposto: '))
h = hypot(ca,co)
print(f'A hipotenusa do cateto oposto de valor {co} e cateto adjacente {ca}, vale {h} ')

