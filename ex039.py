print('='*20,'\nQual o seu sexo: \n [ 1 ] MASCULINO \n [ 2 ] FEMININO \n','='*20)
s= int(input('Escolha a opção: '))
from datetime import date
atual = date.today().year  # colocar o ano atual

if s == 1:
    ano = int(input('Seu alistamento é obrigatório, então, digite o ano em que você nasceu: '))
    if atual - ano == 18:
        print(f'Você tem {atual - ano} anos e deve-se alistar,esse ano, no serviço militar obrigatório')
    elif atual - ano > 18:
        print(f'Você tem {atual - ano} anos e deveria ter se alistado em {atual - ((atual - ano)-18)}, Apresente-se e aliste-se o mais rápido posssível')
    elif atual - ano < 18:
        print(f'Você tem {atual - ano} anos e ainda não deve se alistar, o alistamento militar será no ano de {atual + (18-(atual - ano))}')


elif s == 2:
    print('O alistamento militar não é obrigatório!!')
    ano2= int(input('Se deseja se alistar, digite o ano em que você nasceu: '))
    if atual - ano2 ==18:
        print(f'Você tem {atual-ano2} anos e deve-se alistar, se desejar, esse ano, no serviço militar')
    elif atual - ano2 > 18:
        print(f'Você tem {atual-ano2} anos e deveria ter se alistado, se desejasse, em {atual - ((atual-ano2)-18)}, Apresente-se e aliste-se, se desejar')
    elif atual - ano2 < 18:
        print(f'Você tem {atual-ano2} anos e ainda não deve se alistar, se desejar, em {atual+ (18-(atual-ano2))}')

elif s != 1 or 2:
    print('Valor incorreto, tente novamente !!')






#i= atual-ano

#if i < 18:
 #   print(f'''Quem nasceu em {i} tem {i} anos em {atual}.
#Você só poderá se alistar daqui há {18-i} anos ''')

#elif i> 18:
 #   print(f''' Quem nasceu em {a} tem {i} anos em {atual}.
#Você já deveria ter se alistado há {i-18} anos atrás
#Aliste-se imediatamente!!!''')

#elif i == 18:
 #   print(f'''Quem nasceu em {a} tem {i} anos em {atual}.
#Você deve se alistar esse ano !!! Aliste-se''')

#else:
 #   print('Erro')

