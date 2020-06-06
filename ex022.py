nome= str(input('Digite seu nome completo: ')).strip()
h= nome.upper()
l= nome.lower()
cont= len(nome)
contes= nome.count(' ',0,)
contses= cont-contes
fesp= nome.find(' ')
pnome= nome[0:fesp]
pnomecont= len(pnome)
print(f'Analisando seu nome: \n Seu nome em maiúsculas é {h}\n Seu nome em minúscula é {l}\n Seu nome tem ao todo {contses} letras\n Seu primeiro nome é {pnome} e ele tem {pnomecont} letras')






