pt = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a razão da PA: '))
An= pt+(10-1)*r

for c in range(pt,An+r,r):
    print (c, end='->')