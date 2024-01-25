m = cont = s = maior = menor = 0
r = 'Ss'
while r in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N] ').strip().upper()[0])
m = s / cont
print('Você digitou {} números e a média foi {}'.format(cont, m))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
