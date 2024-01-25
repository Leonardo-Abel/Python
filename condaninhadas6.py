from datetime import date
atual = date.today().year

nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')
