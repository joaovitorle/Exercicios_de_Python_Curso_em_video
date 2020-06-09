s1= float(input('Primeiro segmento: '))
s2= float(input('Segundo segmento: '))
s3= float(input('Terceiro segmento: '))
v= s1<s2+s3 and s2<s1+s3 and s3<s2+s1

if v and s1==s2==s3:
    print('Triângulo equilátero: Todos os lados são iguais')

if v and (s1==s2)!=s3 and (s1==s3)!=s2 and (s2==s3)!=s1:
    print('Triângulo Isósceles: Dois lados são iguais')

if v and s1!=s2!=s3:
    print('Triângulo escaleno: Todos os lados são diferentes')

else:
    print('Os segmentos de reta não formam um Triângulo!')