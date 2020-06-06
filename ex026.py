frase= input('Digite uma frase: ').strip().upper().lower()
cont1= len(frase)
cont2= frase.count('a',0,)
enc= frase.find('a')+1
cont3= frase.rfind('a')+1

print(f' A letra A aparece {cont2}\n A primeira letra A apareceu na posição {enc}\n A última letra A apareceu na posição {cont3}')

