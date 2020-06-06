a= int(input('Digite um valor: '))
b= int(input('Digite,novamente, outro valor: '))
c= int(input('Digite, por fim, outro valor: '))

#Analisando o menor valor
if a<b and a<c:
    print(f'O menor valor digitado é {a}')
elif b<a and b<c:
    print(f'O menor valor digitado é {b}')
else:
    print(f'O menor valor digitado é {c}')
#Analisando o maior valor
if a>b and a>c:
    print(f'O maior valor digitado é {a}')
elif b>a and b>c:
    print(f'O maior valor digitado é {b}')
else:
    print(f'O maior valor digitado é {c}')
    
