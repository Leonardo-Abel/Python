'''
n = m = 0
while n > -1:
    n = int(input('Quer ver a tabuada de qual valor? '))
    cont = 0
    print('-'*20)
    while n > -1:
        cont += 1
        m = cont * n
        print(f'{n} x {cont} = {m}')
        if cont == 10:
            break
    if n < 0:
        print('PROCESSO ENCERRADO. Volte sempre!')
    print('-'*20)
'''
# RESOLUÇÃO GUANABARA
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADA')
