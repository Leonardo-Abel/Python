c = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o valor do seu salário: R$'))
a = int(input('Digite em quantos anos pretende pagar a casa: '))
p = c / (a * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(c, a, p))
if p > (s * 0.3):
    print('Seu empréstimo foi negado.')
else:
    print('Seu empréstimo foi aceito.')
