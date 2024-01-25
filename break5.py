'''total = maismil = menorpreco = count = 0
produto = []
maisbarato = ''
continuar = 'S'

print('-'*40)
print('          LOJA SUPER BARATÃO')
print('-'*40)
while continuar == 'S':
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    count += 1
    total += preco
    if count == 1 or menorpreco > preco:
        menorpreco = preco
        maisbarato = produto
    if preco > 1000:
        maismil += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print('-'*10, ' FIM DO PROGRAMA ', '-'*10)
print(f'O total gasto na compra foi de: R${total:.2f}')
print(f'{maismil} produtos custam mais de R$1000,00')
print(f'O produto mais barato é: {maisbarato}, de R${menorpreco:.2f}')
'''

# GUANABARA
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
