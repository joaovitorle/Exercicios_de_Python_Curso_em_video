s1= int(input('Digite o primeiro segmento de reta: '))
s2= int(input('Digite o segundo segmento de reta: '))
s3= int(input('Digite o terceiro segmento de reta: '))

if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Pode-se formar um triangulo')
else:
    print('Não pode formar um triangulo')
