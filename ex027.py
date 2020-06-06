nome= str(input('Digite seu nome completo: ')).strip()
cont=len(nome)
encon= nome.find(' ')
encon2= nome.rfind(' ')
pnome= nome[0:encon]
unome= nome[encon2:]
print(f' Muito prazer em te conhecer!\n Seu primeiro nome é {pnome}\n Seu último nome é {unome}')
