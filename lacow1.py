'''
r = 'S'
while r == 'S':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor inválido. Digite novamente.')
    else:
        print('O sexo digitado foi {}.'.format(sexo))
print('Fim')
'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')
               ).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
