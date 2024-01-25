print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
'''while True:
    ced50 = int(valor/50)
    valor = valor % 50
    ced20 = int(valor/20)
    valor = valor % 20
    ced10 = int(valor/10)
    valor = valor % 10
    ced1 = valor
    print(f'total de {ced50} de R$50\n'
          f'total de {ced20} de R$20\n'
          f'total de {ced10} de R$10\n'
          f'total de {ced1} de R$1')
    print('='*30)
    break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre!')
