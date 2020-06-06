ano= int(input('Digite qualquer ano e descubra se ele é bissexto: '))
bis= ano % 4
if bis == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
