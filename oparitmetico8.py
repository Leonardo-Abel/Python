p = float(input('Digite o preço do produto: R$'))
# d = p * 0.05
# n = p - d
n = p - (p * 5 / 100)
print('O novo preço do produto, com 5% de desconto é R${:.2f}.'.format(n))
